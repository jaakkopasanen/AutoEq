# Sony MDR-Z1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.8; 23 -2.9; 25 -3.1; 28 -3.2; 31 -3.3; 34 -3.3; 37 -3.4; 41 -3.4; 45 -3.2; 49 -3.0; 54 -3.0; 60 -3.1; 66 -3.3; 72 -3.4; 79 -3.6; 87 -4.3; 96 -4.9; 106 -5.1; 116 -5.2; 128 -5.5; 141 -5.5; 155 -5.2; 170 -4.5; 187 -4.1; 206 -3.6; 227 -3.0; 249 -2.5; 274 -2.1; 302 -1.7; 332 -1.3; 365 -1.0; 402 -0.8; 442 -0.7; 486 -0.5; 535 0.1; 588 0.1; 647 -0.1; 712 -0.2; 783 -0.3; 861 -0.4; 947 -0.2; 1042 0.3; 1146 0.9; 1261 1.2; 1387 1.3; 1526 1.1; 1678 0.5; 1846 -0.4; 2031 -1.3; 2234 -1.2; 2457 -1.4; 2703 0.3; 2973 1.4; 3270 -5.2; 3597 0.4; 3957 6.0; 4353 6.0; 4788 5.3; 5267 3.5; 5793 5.3; 6373 2.8; 7010 -0.5; 7711 0.2; 8482 0.0; 9330 -1.7; 10263 -4.8; 11289 -4.0; 12418 -3.0; 13660 -4.1; 15026 -5.0; 16529 -1.9; 18182 -0.2; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.62 | -2.9 dB |
| Peaking | 133 Hz   |  0.85 | -5.2 dB |
| Peaking | 3314 Hz  |  7.94 | -8.8 dB |
| Peaking | 4565 Hz  |  1.53 | 7.2 dB  |
| Peaking | 13083 Hz |  0.74 | -4.6 dB |
| Peaking | 1390 Hz  |  2.65 | 1.6 dB  |
| Peaking | 2276 Hz  |  2.46 | -2.6 dB |
| Peaking | 2890 Hz  | 11.1  | 2.7 dB  |
| Peaking | 9998 Hz  |  1.92 | 2.9 dB  |
| Peaking | 10325 Hz |  4.48 | -5.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-Z1R/Sony%20MDR-Z1R.png)