# Etymotic ER4XR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.8; 87 5.2; 96 4.6; 106 3.7; 116 2.9; 128 2.1; 141 1.4; 155 0.9; 170 0.5; 187 0.1; 206 -0.3; 227 -0.5; 249 -0.5; 274 -0.3; 302 -0.0; 332 0.1; 365 0.2; 402 0.4; 442 0.5; 486 0.8; 535 1.0; 588 1.2; 647 1.5; 712 1.6; 783 1.4; 861 1.0; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.6; 1387 -2.5; 1526 -3.4; 1678 -3.9; 1846 -4.0; 2031 -3.8; 2234 -3.2; 2457 -2.3; 2703 -1.4; 2973 -0.6; 3270 0.1; 3597 0.0; 3957 -1.4; 4353 -3.1; 4788 -1.8; 5267 1.7; 5793 5.1; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.52 | 6.9 dB  |
| Peaking | 726 Hz  | 2.14 | 2.0 dB  |
| Peaking | 1794 Hz | 1.66 | -4.4 dB |
| Peaking | 4492 Hz | 5.75 | -4.0 dB |
| Peaking | 6087 Hz | 4.03 | 6.7 dB  |
| Peaking | 17 Hz   | 1.11 | 2.5 dB  |
| Peaking | 40 Hz   | 1.09 | -1.5 dB |
| Peaking | 80 Hz   | 1.83 | 1.8 dB  |
| Peaking | 208 Hz  | 1.57 | -1.6 dB |
| Peaking | 3367 Hz | 6.67 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Etymotic%20ER4XR/Etymotic%20ER4XR.png)