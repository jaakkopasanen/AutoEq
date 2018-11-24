# Sennheiser HD 800 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 5.0; 25 4.9; 28 4.6; 31 4.5; 34 4.3; 37 4.2; 41 4.0; 45 3.8; 49 3.6; 54 3.3; 60 2.9; 66 2.5; 72 2.1; 79 1.6; 87 1.1; 96 0.7; 106 0.1; 116 -0.3; 128 -0.8; 141 -1.1; 155 -1.4; 170 -1.6; 187 -1.7; 206 -1.7; 227 -1.6; 249 -1.6; 274 -1.6; 302 -1.7; 332 -1.7; 365 -1.7; 402 -1.7; 442 -1.7; 486 -1.7; 535 -1.6; 588 -1.4; 647 -1.2; 712 -0.9; 783 -0.6; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.7; 1387 0.9; 1526 1.3; 1678 1.3; 1846 0.1; 2031 -0.8; 2234 0.2; 2457 0.8; 2703 2.0; 2973 1.6; 3270 2.1; 3597 0.3; 3957 -0.1; 4353 1.4; 4788 2.5; 5267 2.1; 5793 -0.2; 6373 -2.9; 7010 -1.7; 7711 -0.8; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.6; 13660 -0.1; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.26 | 5.1 dB  |
| Peaking | 51 Hz   | 1.96 | 2.9 dB  |
| Peaking | 2927 Hz | 3.78 | 2.1 dB  |
| Peaking | 4980 Hz | 4.81 | 3.2 dB  |
| Peaking | 6487 Hz | 4.57 | -3.3 dB |
| Peaking | 36 Hz   | 2.71 | 1.2 dB  |
| Peaking | 79 Hz   | 1.36 | 2.3 dB  |
| Peaking | 199 Hz  | 0.23 | -2.0 dB |
| Peaking | 1482 Hz | 1.32 | 1.8 dB  |
| Peaking | 2011 Hz | 5.63 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)