# Sennheiser HD 202 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.3; 25 3.6; 28 2.7; 31 1.9; 34 1.2; 37 0.6; 41 -0.1; 45 -0.7; 49 -1.3; 54 -2.0; 60 -2.6; 66 -3.0; 72 -3.0; 79 -2.9; 87 -3.0; 96 -3.0; 106 -2.8; 116 -2.4; 128 -1.9; 141 -1.3; 155 -0.7; 170 0.1; 187 0.9; 206 1.9; 227 3.0; 249 4.2; 274 5.3; 302 5.7; 332 4.8; 365 4.7; 402 4.7; 442 4.4; 486 3.7; 535 3.0; 588 2.3; 647 2.0; 712 1.6; 783 1.1; 861 0.6; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.6; 1526 -2.2; 1678 -2.0; 1846 -1.0; 2031 0.4; 2234 1.6; 2457 2.6; 2703 4.4; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.62 | 6.5 dB  |
| Peaking | 88 Hz   | 0.39 | -4.8 dB |
| Peaking | 306 Hz  | 0.84 | 7.1 dB  |
| Peaking | 1593 Hz | 1.71 | -4.1 dB |
| Peaking | 3914 Hz | 0.93 | 7.1 dB  |
| Peaking | 203 Hz  | 0.71 | 0.1 dB  |
| Peaking | 2956 Hz | 6.13 | 1.4 dB  |
| Peaking | 3944 Hz | 2.82 | -1.0 dB |
| Peaking | 6260 Hz | 2.55 | 5.1 dB  |
| Peaking | 7405 Hz | 1.52 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20202%20II/Sennheiser%20HD%20202%20II.png)