# Sennheiser HD 800 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 5.0; 25 4.9; 28 4.6; 31 4.5; 34 4.3; 37 4.2; 41 4.0; 45 3.8; 49 3.6; 54 3.3; 60 2.9; 66 2.5; 72 2.1; 79 1.6; 87 1.1; 96 0.7; 106 0.1; 116 -0.3; 128 -0.8; 141 -1.1; 155 -1.4; 170 -1.6; 187 -1.7; 206 -1.7; 227 -1.6; 249 -1.6; 274 -1.6; 302 -1.7; 332 -1.7; 365 -1.7; 402 -1.7; 442 -1.7; 486 -1.7; 535 -1.6; 588 -1.4; 647 -1.2; 712 -0.9; 783 -0.6; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.7; 1387 0.9; 1526 1.3; 1678 1.3; 1846 0.1; 2031 -0.8; 2234 0.2; 2457 0.8; 2703 1.8; 2973 1.2; 3270 1.3; 3597 -0.7; 3957 -1.4; 4353 0.1; 4788 0.7; 5267 -0.5; 5793 -2.7; 6373 -4.1; 7010 -2.3; 7711 -1.2; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -3.8; 13660 -2.9; 15026 -0.1; 16529 0.0; 18182 -2.1; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.6  | 4.8 dB  |
| Peaking | 54 Hz    | 0.85 | 2.3 dB  |
| Peaking | 225 Hz   | 0.52 | -2.2 dB |
| Peaking | 6391 Hz  | 4.81 | -4.3 dB |
| Peaking | 20303 Hz | 1.41 | -8.0 dB |
| Peaking | 1486 Hz  | 3.46 | 1.5 dB  |
| Peaking | 2809 Hz  | 4.97 | 1.9 dB  |
| Peaking | 11423 Hz | 2.82 | 2.0 dB  |
| Peaking | 12748 Hz | 3.26 | -5.6 dB |
| Peaking | 15952 Hz | 1.49 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)