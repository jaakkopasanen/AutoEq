# Hifiman HE350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.5; 37 -1.8; 41 -2.3; 45 -2.8; 49 -3.2; 54 -3.6; 60 -4.1; 66 -4.4; 72 -4.6; 79 -4.6; 87 -4.9; 96 -5.6; 106 -6.0; 116 -6.4; 128 -7.0; 141 -7.6; 155 -7.8; 170 -7.9; 187 -7.8; 206 -7.8; 227 -7.9; 249 -7.7; 274 -7.2; 302 -6.7; 332 -6.4; 365 -6.0; 402 -5.7; 442 -5.8; 486 -6.2; 535 -6.2; 588 -6.2; 647 -5.9; 712 -5.7; 783 -6.0; 861 -6.4; 947 -6.5; 1042 -6.4; 1146 -6.2; 1261 -5.7; 1387 -5.1; 1526 -4.5; 1678 -3.9; 1846 -2.9; 2031 -1.9; 2234 -2.2; 2457 -3.5; 2703 -4.3; 2973 -4.4; 3270 -4.6; 3597 -5.7; 3957 -7.7; 4353 -9.5; 4788 -10.8; 5267 -11.9; 5793 -11.9; 6373 -10.1; 7010 -6.9; 7711 -6.2; 8482 -6.5; 9330 -9.0; 10263 -11.3; 11289 -12.3; 12418 -13.3; 13660 -13.9; 15026 -11.7; 16529 -7.3; 18182 -6.5; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman HE350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman HE350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.14 | 6.0 dB  |
| Peaking | 48 Hz    | 1.55 | 2.0 dB  |
| Peaking | 2157 Hz  | 1.55 | 4.6 dB  |
| Peaking | 5261 Hz  | 2.97 | -6.1 dB |
| Peaking | 13063 Hz | 1.52 | -8.0 dB |
| Peaking | 184 Hz   | 1.89 | -1.8 dB |
| Peaking | 6226 Hz  | 5.29 | -2.5 dB |
| Peaking | 7698 Hz  | 2.22 | 2.8 dB  |
| Peaking | 10292 Hz | 3.91 | -2.4 dB |
| Peaking | 17442 Hz | 3.65 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -5.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20HE350/Hifiman%20HE350.png)