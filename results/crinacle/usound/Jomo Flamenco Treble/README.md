# Jomo Flamenco Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.1; 34 -1.4; 37 -1.7; 41 -2.1; 45 -2.3; 49 -2.6; 54 -2.9; 60 -3.3; 66 -3.7; 72 -4.0; 79 -4.5; 87 -4.9; 96 -5.4; 106 -5.9; 116 -6.2; 128 -6.6; 141 -6.9; 155 -7.2; 170 -7.3; 187 -7.5; 206 -7.5; 227 -7.5; 249 -7.5; 274 -7.3; 302 -7.2; 332 -7.0; 365 -6.7; 402 -6.5; 442 -6.2; 486 -5.7; 535 -5.3; 588 -4.7; 647 -4.1; 712 -3.4; 783 -2.7; 861 -2.0; 947 -1.7; 1042 -2.0; 1146 -2.7; 1261 -3.7; 1387 -4.5; 1526 -4.9; 1678 -5.3; 1846 -5.9; 2031 -6.9; 2234 -7.7; 2457 -7.5; 2703 -6.5; 2973 -6.1; 3270 -6.7; 3597 -7.3; 3957 -6.5; 4353 -6.8; 4788 -9.2; 5267 -11.6; 5793 -11.8; 6373 -12.0; 7010 -13.5; 7711 -12.4; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.0; 16529 -10.0; 18182 -7.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.06 | 6.0 dB  |
| Peaking | 54 Hz    | 1.74 | 2.5 dB  |
| Peaking | 945 Hz   | 1.68 | 5.1 dB  |
| Peaking | 6537 Hz  | 2.12 | -7.0 dB |
| Peaking | 16590 Hz | 2.82 | -4.0 dB |
| Peaking | 218 Hz   | 1.35 | -1.4 dB |
| Peaking | 2275 Hz  | 5.04 | -1.9 dB |
| Peaking | 5319 Hz  | 4.25 | -4.4 dB |
| Peaking | 6845 Hz  | 1.04 | 3.8 dB  |
| Peaking | 7443 Hz  | 4.92 | -5.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Flamenco%20Treble/Jomo%20Flamenco%20Treble.png)