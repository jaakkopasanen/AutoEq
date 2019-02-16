# Quad Era-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.7; 49 -0.8; 54 -1.1; 60 -1.4; 66 -1.5; 72 -1.7; 79 -2.0; 87 -2.4; 96 -2.7; 106 -3.1; 116 -3.4; 128 -3.9; 141 -4.3; 155 -4.4; 170 -4.3; 187 -4.2; 206 -4.2; 227 -4.1; 249 -3.7; 274 -3.6; 302 -3.6; 332 -3.7; 365 -3.2; 402 -3.0; 442 -2.9; 486 -2.8; 535 -2.6; 588 -2.8; 647 -2.9; 712 -3.4; 783 -3.9; 861 -4.8; 947 -6.1; 1042 -6.4; 1146 -5.4; 1261 -3.6; 1387 -1.4; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.3; 6373 -4.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.0; 18182 -11.0; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Quad Era-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Quad Era-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.29 | 6.1 dB  |
| Peaking | 457 Hz   | 1.08 | 3.5 dB  |
| Peaking | 1881 Hz  | 1.49 | 5.2 dB  |
| Peaking | 4175 Hz  | 1.09 | 6.0 dB  |
| Peaking | 18622 Hz | 1.04 | -5.0 dB |
| Peaking | 718 Hz   | 2.88 | 1.2 dB  |
| Peaking | 1030 Hz  | 2.96 | -2.6 dB |
| Peaking | 1427 Hz  | 6.06 | 2.2 dB  |
| Peaking | 5527 Hz  | 8.28 | 1.9 dB  |
| Peaking | 8283 Hz  | 3.17 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Quad%20Era-1/Quad%20Era-1.png)