# JBL T450BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.9; 25 1.4; 28 0.7; 31 0.1; 34 -0.3; 37 -0.7; 41 -1.1; 45 -1.4; 49 -1.6; 54 -1.9; 60 -2.3; 66 -2.9; 72 -3.4; 79 -3.8; 87 -4.2; 96 -4.5; 106 -4.8; 116 -5.0; 128 -5.0; 141 -5.0; 155 -5.0; 170 -4.8; 187 -4.5; 206 -4.0; 227 -3.3; 249 -2.5; 274 -1.6; 302 -0.7; 332 -0.8; 365 -0.2; 402 0.7; 442 0.6; 486 0.3; 535 0.1; 588 -0.0; 647 -0.2; 712 -0.2; 783 -0.2; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.5; 1387 0.4; 1526 0.5; 1678 0.7; 1846 1.0; 2031 1.3; 2234 2.4; 2457 2.2; 2703 1.6; 2973 0.4; 3270 -0.3; 3597 0.5; 3957 1.9; 4353 2.9; 4788 4.7; 5267 6.0; 5793 5.6; 6373 3.5; 7010 0.7; 7711 -3.2; 8482 -5.6; 9330 -6.6; 10263 -5.0; 11289 -2.8; 12418 -1.6; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL T450BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL T450BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.05 | 2.7 dB  |
| Peaking | 101 Hz   | 0.97 | -4.3 dB |
| Peaking | 179 Hz   | 1.85 | -3.1 dB |
| Peaking | 5599 Hz  | 1.81 | 7.5 dB  |
| Peaking | 8954 Hz  | 1.97 | -8.4 dB |
| Peaking | 233 Hz   | 5.52 | -0.6 dB |
| Peaking | 421 Hz   | 3.82 | 1.3 dB  |
| Peaking | 2385 Hz  | 2.37 | 2.2 dB  |
| Peaking | 3271 Hz  | 3.93 | -2.1 dB |
| Peaking | 13985 Hz | 4.26 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20T450BT/JBL%20T450BT.png)