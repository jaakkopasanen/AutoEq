# Warbler Prelude
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.8; 25 -1.3; 28 -2.1; 31 -2.8; 34 -3.5; 37 -4.0; 41 -4.6; 45 -5.1; 49 -5.6; 54 -6.1; 60 -6.6; 66 -7.2; 72 -7.8; 79 -8.3; 87 -8.8; 96 -9.4; 106 -9.9; 116 -10.4; 128 -10.8; 141 -11.3; 155 -11.5; 170 -11.8; 187 -12.0; 206 -12.1; 227 -12.2; 249 -12.2; 274 -12.2; 302 -12.1; 332 -11.9; 365 -11.6; 402 -11.5; 442 -11.3; 486 -11.0; 535 -10.7; 588 -10.3; 647 -9.9; 712 -9.4; 783 -8.9; 861 -8.4; 947 -8.2; 1042 -8.3; 1146 -8.7; 1261 -9.0; 1387 -8.8; 1526 -8.3; 1678 -7.4; 1846 -6.5; 2031 -5.5; 2234 -4.5; 2457 -3.9; 2703 -3.9; 2973 -4.4; 3270 -4.4; 3597 -3.2; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -11.3; 16529 -7.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Warbler Prelude GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Warbler Prelude ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.34 | 7.3 dB  |
| Peaking | 239 Hz   | 0.32 | -5.8 dB |
| Peaking | 2432 Hz  | 3.9  | 2.3 dB  |
| Peaking | 4918 Hz  | 1.55 | 7.0 dB  |
| Peaking | 15083 Hz | 3.81 | -5.3 dB |
| Peaking | 919 Hz   | 2.04 | 1.1 dB  |
| Peaking | 1352 Hz  | 2.08 | -1.8 dB |
| Peaking | 2011 Hz  | 2.99 | 0.7 dB  |
| Peaking | 6464 Hz  | 4.93 | 3.2 dB  |
| Peaking | 7518 Hz  | 2.13 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Warbler%20Prelude/Warbler%20Prelude.png)