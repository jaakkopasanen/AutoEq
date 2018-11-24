# Sennheiser HD 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.6; 41 4.9; 45 4.2; 49 3.7; 54 3.1; 60 2.6; 66 2.0; 72 1.6; 79 1.2; 87 0.8; 96 0.3; 106 -0.1; 116 -0.5; 128 -0.9; 141 -1.2; 155 -1.3; 170 -1.4; 187 -1.4; 206 -1.3; 227 -1.1; 249 -0.8; 274 -0.6; 302 -0.3; 332 -0.2; 365 -0.1; 402 -0.0; 442 -0.0; 486 0.0; 535 0.1; 588 0.1; 647 0.2; 712 0.1; 783 -0.2; 861 -0.5; 947 -0.4; 1042 -0.3; 1146 -0.7; 1261 -1.2; 1387 -2.1; 1526 -2.9; 1678 -3.4; 1846 -3.4; 2031 -3.3; 2234 -2.3; 2457 -2.1; 2703 -1.7; 2973 -1.7; 3270 -1.3; 3597 -0.6; 3957 -0.5; 4353 -0.2; 4788 0.1; 5267 1.4; 5793 3.2; 6373 2.6; 7010 2.0; 7711 0.3; 8482 -0.7; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.64 | 6.4 dB  |
| Peaking | 154 Hz  | 1.12 | -2.0 dB |
| Peaking | 1747 Hz | 2.18 | -3.2 dB |
| Peaking | 2739 Hz | 1.25 | -1.3 dB |
| Peaking | 6026 Hz | 3.62 | 3.7 dB  |
| Peaking | 592 Hz  | 1.75 | 0.3 dB  |
| Peaking | 8520 Hz | 8.73 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)