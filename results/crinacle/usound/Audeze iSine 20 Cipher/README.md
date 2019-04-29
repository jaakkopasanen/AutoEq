# Audeze iSine 20 Cipher
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -6.2; 25 -7.1; 28 -8.0; 31 -8.5; 34 -8.6; 37 -8.4; 41 -8.1; 45 -8.0; 49 -8.1; 54 -8.4; 60 -8.6; 66 -8.6; 72 -8.4; 79 -8.1; 87 -7.7; 96 -7.4; 106 -7.2; 116 -7.5; 128 -8.0; 141 -7.8; 155 -7.2; 170 -6.5; 187 -6.1; 206 -6.0; 227 -6.3; 249 -6.5; 274 -6.4; 302 -6.1; 332 -5.7; 365 -5.3; 402 -5.2; 442 -5.4; 486 -5.7; 535 -6.0; 588 -6.1; 647 -6.1; 712 -6.2; 783 -6.3; 861 -6.5; 947 -6.9; 1042 -6.9; 1146 -7.0; 1261 -7.6; 1387 -8.7; 1526 -10.2; 1678 -10.0; 1846 -9.5; 2031 -8.7; 2234 -8.7; 2457 -9.6; 2703 -9.2; 2973 -7.9; 3270 -8.2; 3597 -7.8; 3957 -4.9; 4353 -4.8; 4788 -5.8; 5267 -3.5; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.4; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.8; 15026 -9.8; 16529 -9.6; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine 20 Cipher GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine 20 Cipher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 54 Hz    |  0.78 | -2.2 dB |
| Peaking | 1607 Hz  |  3.19 | -3.7 dB |
| Peaking | 2574 Hz  |  2.44 | -2.9 dB |
| Peaking | 6077 Hz  |  3.64 | 6.7 dB  |
| Peaking | 15946 Hz |  2.66 | -4.4 dB |
| Peaking | 136 Hz   |  5.05 | -1.2 dB |
| Peaking | 192 Hz   |  4.92 | 0.7 dB  |
| Peaking | 405 Hz   |  2.08 | 1.3 dB  |
| Peaking | 4145 Hz  | 11.86 | 2.2 dB  |
| Peaking | 7879 Hz  |  6.82 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audeze%20iSine%2020%20Cipher/Audeze%20iSine%2020%20Cipher.png)