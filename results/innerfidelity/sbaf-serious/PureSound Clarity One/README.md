# PureSound Clarity One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.1dB
GraphicEQ: 21 -4.2; 23 -4.6; 25 -5.0; 28 -5.7; 31 -6.2; 34 -6.6; 37 -7.0; 41 -7.4; 45 -7.8; 49 -8.1; 54 -8.5; 60 -8.9; 66 -9.3; 72 -9.6; 79 -9.9; 87 -10.2; 96 -10.5; 106 -10.6; 116 -10.6; 128 -10.7; 141 -10.6; 155 -10.5; 170 -10.3; 187 -9.9; 206 -9.6; 227 -9.1; 249 -8.6; 274 -8.0; 302 -7.4; 332 -6.8; 365 -6.1; 402 -5.4; 442 -4.5; 486 -4.0; 535 -3.3; 588 -2.3; 647 -1.6; 712 -1.2; 783 -0.5; 861 -0.3; 947 -0.0; 1042 0.0; 1146 -0.1; 1261 -0.4; 1387 -1.0; 1526 -2.0; 1678 -2.6; 1846 -2.6; 2031 -2.2; 2234 -2.0; 2457 -1.5; 2703 -1.7; 2973 -2.2; 3270 -2.9; 3597 -3.3; 3957 -3.4; 4353 -4.9; 4788 -5.6; 5267 -6.1; 5793 -9.6; 6373 -13.6; 7010 -8.6; 7711 -4.7; 8482 -3.1; 9330 -4.0; 10263 -4.2; 11289 -1.0; 12418 0.0; 13660 0.0; 15026 -0.7; 16529 -3.5; 18182 -1.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PureSound Clarity One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PureSound Clarity One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.39 | -6.4 dB  |
| Peaking | 145 Hz   | 0.63 | -6.4 dB  |
| Peaking | 303 Hz   | 1.03 | -3.2 dB  |
| Peaking | 6215 Hz  | 1.81 | -11.7 dB |
| Peaking | 16855 Hz | 3.47 | -3.8 dB  |
| Peaking | 1867 Hz  | 2.84 | -2.1 dB  |
| Peaking | 8094 Hz  | 5.39 | 2.4 dB   |
| Peaking | 10159 Hz | 3.26 | -3.5 dB  |
| Peaking | 11966 Hz | 1.94 | 2.3 dB   |
| Peaking | 16089 Hz | 2.99 | -0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PureSound%20Clarity%20One/PureSound%20Clarity%20One.png)