# Audeze LCD-2 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.0; 25 -3.2; 28 -3.4; 31 -3.6; 34 -3.8; 37 -3.9; 41 -4.0; 45 -4.1; 49 -4.2; 54 -4.4; 60 -4.7; 66 -5.1; 72 -5.3; 79 -5.6; 87 -5.9; 96 -6.3; 106 -6.7; 116 -7.0; 128 -7.3; 141 -7.6; 155 -7.9; 170 -8.1; 187 -8.4; 206 -8.6; 227 -8.7; 249 -8.8; 274 -8.9; 302 -8.9; 332 -8.9; 365 -8.7; 402 -8.5; 442 -8.1; 486 -7.9; 535 -8.1; 588 -8.6; 647 -9.2; 712 -9.9; 783 -10.5; 861 -10.4; 947 -9.7; 1042 -10.0; 1146 -9.9; 1261 -9.7; 1387 -8.9; 1526 -7.8; 1678 -7.0; 1846 -6.1; 2031 -4.7; 2234 -5.5; 2457 -7.0; 2703 -6.4; 2973 -4.4; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -6.7; 6373 -7.5; 7010 -7.2; 7711 -9.4; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -14.2; 13660 -14.8; 15026 -7.1; 16529 -6.5; 18182 -6.5; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.25 | 3.5 dB   |
| Peaking | 225 Hz   | 0.71 | -2.4 dB  |
| Peaking | 935 Hz   | 1.23 | -3.9 dB  |
| Peaking | 4017 Hz  | 2.08 | 7.3 dB   |
| Peaking | 13173 Hz | 3.75 | -10.6 dB |
| Peaking | 2054 Hz  | 5.51 | 2.2 dB   |
| Peaking | 2536 Hz  | 7.44 | -2.0 dB  |
| Peaking | 5083 Hz  | 6.24 | 4.0 dB   |
| Peaking | 6932 Hz  | 1.44 | -2.9 dB  |
| Peaking | 10191 Hz | 2.55 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)