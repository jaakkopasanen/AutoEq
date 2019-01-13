# Sony IER-M7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.4; 23 -1.6; 25 -1.7; 28 -1.8; 31 -1.9; 34 -2.0; 37 -2.1; 41 -2.2; 45 -2.3; 49 -2.4; 54 -2.5; 60 -2.7; 66 -2.8; 72 -3.0; 79 -3.2; 87 -3.4; 96 -3.6; 106 -3.8; 116 -3.9; 128 -3.9; 141 -4.0; 155 -4.0; 170 -3.9; 187 -3.8; 206 -3.7; 227 -3.5; 249 -3.3; 274 -3.1; 302 -2.8; 332 -2.5; 365 -2.1; 402 -1.9; 442 -1.7; 486 -1.3; 535 -1.0; 588 -0.7; 647 -0.4; 712 -0.1; 783 0.2; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.4; 1387 -0.2; 1526 0.2; 1678 0.7; 1846 1.2; 2031 1.9; 2234 2.7; 2457 3.6; 2703 4.8; 2973 5.5; 3270 4.7; 3597 3.9; 3957 5.1; 4353 5.1; 4788 4.5; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -2.3; 10263 -4.3; 11289 -6.0; 12418 -7.0; 13660 -9.0; 15026 -14.3; 16529 -19.4; 18182 -18.0; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 52 Hz    | 0.29 | -1.8 dB  |
| Peaking | 178 Hz   | 0.56 | -3.0 dB  |
| Peaking | 2902 Hz  | 1.91 | 4.4 dB   |
| Peaking | 5754 Hz  | 1.33 | 7.3 dB   |
| Peaking | 17143 Hz | 0.93 | -21.0 dB |
| Peaking | 837 Hz   | 1.85 | 1.4 dB   |
| Peaking | 1300 Hz  | 0.9  | -1.4 dB  |
| Peaking | 1821 Hz  | 1.28 | 0.8 dB   |
| Peaking | 18846 Hz | 3.7  | -2.1 dB  |
| Peaking | 20315 Hz | 1.89 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20IER-M7/Sony%20IER-M7.png)