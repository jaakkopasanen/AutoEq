# Pioneer Monitor 10 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.5; 60 4.9; 66 4.3; 72 3.8; 79 3.2; 87 2.7; 96 2.3; 106 1.5; 116 0.4; 128 -1.0; 141 -2.1; 155 -3.2; 170 -4.3; 187 -5.1; 206 -5.9; 227 -6.4; 249 -6.6; 274 -7.1; 302 -7.7; 332 -7.5; 365 -7.2; 402 -6.7; 442 -6.1; 486 -5.4; 535 -4.5; 588 -3.4; 647 -2.3; 712 -1.3; 783 -0.8; 861 -0.2; 947 -0.0; 1042 0.0; 1146 0.1; 1261 0.2; 1387 0.3; 1526 0.1; 1678 0.7; 1846 3.3; 2031 5.6; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -3.8; 15026 -8.6; 16529 -9.8; 18182 -8.5; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer Monitor 10 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.36 | 6.7 dB   |
| Peaking | 278 Hz   | 0.69 | -8.7 dB  |
| Peaking | 2284 Hz  | 2.76 | 3.9 dB   |
| Peaking | 4441 Hz  | 0.76 | 6.6 dB   |
| Peaking | 17768 Hz | 0.8  | -10.5 dB |
| Peaking | 849 Hz   | 3.2  | 1.3 dB   |
| Peaking | 1576 Hz  | 6.75 | -1.7 dB  |
| Peaking | 6412 Hz  | 4.22 | 2.8 dB   |
| Peaking | 7502 Hz  | 2.77 | -2.8 dB  |
| Peaking | 12243 Hz | 4.77 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Pioneer%20Monitor%2010%20II/Pioneer%20Monitor%2010%20II.png)