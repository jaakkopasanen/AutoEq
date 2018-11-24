# JBL Everest Elite 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.0; 25 -1.1; 28 -1.2; 31 -1.2; 34 -1.1; 37 -1.0; 41 -0.8; 45 -0.7; 49 -0.6; 54 -0.5; 60 -0.4; 66 -0.3; 72 -0.1; 79 -0.0; 87 -0.0; 96 0.1; 106 0.0; 116 0.0; 128 0.0; 141 0.0; 155 -0.0; 170 -0.1; 187 -0.1; 206 -0.2; 227 -0.2; 249 -0.2; 274 -0.1; 302 0.0; 332 0.2; 365 0.5; 402 0.3; 442 -0.1; 486 -0.4; 535 -0.6; 588 -0.6; 647 -0.3; 712 0.1; 783 0.3; 861 0.2; 947 0.0; 1042 0.1; 1146 0.3; 1261 -1.1; 1387 -2.6; 1526 -2.3; 1678 -1.9; 1846 -2.6; 2031 -2.9; 2234 -2.9; 2457 -2.5; 2703 -2.0; 2973 -1.8; 3270 -1.2; 3597 0.0; 3957 0.8; 4353 2.3; 4788 5.8; 5267 6.0; 5793 3.3; 6373 0.4; 7010 1.1; 7711 0.3; 8482 -1.6; 9330 -7.0; 10263 -9.5; 11289 -8.8; 12418 -5.4; 13660 -0.5; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.81 | -1.2 dB  |
| Peaking | 93 Hz    | 1.85 | 0.2 dB   |
| Peaking | 2197 Hz  | 1.19 | -3.2 dB  |
| Peaking | 5116 Hz  | 2.86 | 7.4 dB   |
| Peaking | 10619 Hz | 2.73 | -10.9 dB |
| Peaking | 1196 Hz  | 2.05 | 1.4 dB   |
| Peaking | 1385 Hz  | 5.15 | -2.4 dB  |
| Peaking | 7894 Hz  | 4.43 | 3.7 dB   |
| Peaking | 8619 Hz  | 1.78 | -1.7 dB  |
| Peaking | 11555 Hz | 2.31 | 0.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/JBL%20Everest%20Elite%20700/JBL%20Everest%20Elite%20700.png)