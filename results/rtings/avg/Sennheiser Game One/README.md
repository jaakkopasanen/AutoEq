# Sennheiser Game One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.5; 45 5.0; 49 4.6; 54 4.1; 60 3.5; 66 2.9; 72 2.4; 79 1.9; 87 1.3; 96 0.7; 106 0.2; 116 -0.3; 128 -0.8; 141 -1.1; 155 -1.3; 170 -1.4; 187 -1.4; 206 -1.3; 227 -1.1; 249 -1.1; 274 -1.1; 302 -1.1; 332 -1.1; 365 -1.0; 402 -1.0; 442 -1.1; 486 -1.1; 535 -0.9; 588 -0.8; 647 -0.6; 712 -0.1; 783 0.1; 861 0.1; 947 0.1; 1042 -0.0; 1146 0.1; 1261 -0.2; 1387 -0.3; 1526 0.1; 1678 -0.2; 1846 -0.5; 2031 -1.3; 2234 -1.6; 2457 -1.1; 2703 -0.7; 2973 -0.4; 3270 0.1; 3597 0.9; 3957 2.5; 4353 1.4; 4788 -0.1; 5267 1.5; 5793 1.6; 6373 0.1; 7010 -0.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.8; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Game One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Game One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.35 | 6.9 dB  |
| Peaking | 126 Hz   | 0.46 | -3.3 dB |
| Peaking | 2253 Hz  | 3.42 | -1.6 dB |
| Peaking | 4010 Hz  | 7.09 | 2.9 dB  |
| Peaking | 5584 Hz  | 7.36 | 1.9 dB  |
| Peaking | 244 Hz   | 3.78 | 0.4 dB  |
| Peaking | 549 Hz   | 1.79 | -0.7 dB |
| Peaking | 778 Hz   | 1.57 | 0.6 dB  |
| Peaking | 19506 Hz | 2.28 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Game%20One/Sennheiser%20Game%20One.png)