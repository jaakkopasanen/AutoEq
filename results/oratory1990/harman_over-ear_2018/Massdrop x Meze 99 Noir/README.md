# Massdrop x Meze 99 Noir
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -14.1; 25 -14.2; 28 -14.3; 31 -14.4; 34 -14.4; 37 -14.5; 41 -14.5; 45 -14.6; 49 -14.6; 54 -14.5; 60 -14.3; 66 -14.1; 72 -13.8; 79 -13.9; 87 -14.1; 96 -13.1; 106 -12.5; 116 -12.9; 128 -13.6; 141 -14.1; 155 -14.0; 170 -13.6; 187 -12.5; 206 -11.3; 227 -10.3; 249 -9.0; 274 -7.0; 302 -4.9; 332 -3.1; 365 -2.3; 402 -2.8; 442 -3.7; 486 -4.7; 535 -5.5; 588 -5.9; 647 -6.0; 712 -6.0; 783 -6.0; 861 -6.0; 947 -6.2; 1042 -6.3; 1146 -6.8; 1261 -7.1; 1387 -7.1; 1526 -6.8; 1678 -6.1; 1846 -5.3; 2031 -4.5; 2234 -4.0; 2457 -3.7; 2703 -3.6; 2973 -3.4; 3270 -2.6; 3597 -0.6; 3957 -0.5; 4353 -0.9; 4788 -4.5; 5267 -6.9; 5793 -7.3; 6373 -7.7; 7010 -8.9; 7711 -10.3; 8482 -8.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.3; 13660 -8.8; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Meze 99 Noir GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Meze 99 Noir ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 12 Hz    |  0.43 | -6.5 dB |
| Peaking | 56 Hz    |  0.54 | -6.0 dB |
| Peaking | 168 Hz   |  1.16 | -5.6 dB |
| Peaking | 361 Hz   |  1.91 | 6.0 dB  |
| Peaking | 3685 Hz  |  2.53 | 6.5 dB  |
| Peaking | 1362 Hz  |  3.8  | -1.1 dB |
| Peaking | 2264 Hz  |  3.13 | 2.0 dB  |
| Peaking | 4343 Hz  | 10.23 | 2.7 dB  |
| Peaking | 7296 Hz  |  2.05 | -3.4 dB |
| Peaking | 19899 Hz |  1.09 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Meze%2099%20Noir/Massdrop%20x%20Meze%2099%20Noir.png)