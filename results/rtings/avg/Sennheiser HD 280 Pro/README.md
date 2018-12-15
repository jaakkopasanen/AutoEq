# Sennheiser HD 280 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 -1.3; 23 -1.6; 25 -2.0; 28 -2.4; 31 -2.8; 34 -3.0; 37 -3.0; 41 -2.8; 45 -2.6; 49 -2.2; 54 -1.7; 60 -1.1; 66 -0.6; 72 -0.1; 79 0.4; 87 0.7; 96 0.9; 106 1.0; 116 1.4; 128 2.0; 141 2.9; 155 3.7; 170 3.8; 187 2.8; 206 1.4; 227 0.0; 249 -0.8; 274 -1.6; 302 -2.1; 332 -2.5; 365 -2.8; 402 -3.3; 442 -3.2; 486 -2.7; 535 -2.4; 588 -2.1; 647 -1.7; 712 -1.3; 783 -1.1; 861 -0.8; 947 -0.2; 1042 -0.0; 1146 -0.2; 1261 -0.2; 1387 -0.1; 1526 0.0; 1678 -0.1; 1846 -0.2; 2031 -0.4; 2234 0.3; 2457 2.1; 2703 3.9; 2973 5.0; 3270 3.2; 3597 2.1; 3957 3.2; 4353 4.2; 4788 1.1; 5267 1.5; 5793 1.1; 6373 0.3; 7010 1.9; 7711 0.2; 8482 -2.9; 9330 -2.8; 10263 -0.1; 11289 -0.1; 12418 -0.2; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 1.23 | -3.3 dB |
| Peaking | 163 Hz  | 1.58 | 4.8 dB  |
| Peaking | 379 Hz  | 0.92 | -3.6 dB |
| Peaking | 2900 Hz | 4.38 | 5.2 dB  |
| Peaking | 4214 Hz | 4.69 | 3.9 dB  |
| Peaking | 235 Hz  | 5.96 | -0.3 dB |
| Peaking | 1000 Hz | 5.25 | 0.6 dB  |
| Peaking | 2023 Hz | 7.47 | -0.9 dB |
| Peaking | 7074 Hz | 4.98 | 2.0 dB  |
| Peaking | 8823 Hz | 5.25 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)