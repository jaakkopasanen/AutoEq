# Audeze Sine (Cipher Cable)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -2.9; 25 -2.9; 28 -2.8; 31 -2.8; 34 -2.8; 37 -2.8; 41 -2.8; 45 -3.1; 49 -3.3; 54 -3.5; 60 -3.8; 66 -4.2; 72 -4.6; 79 -4.7; 87 -4.9; 96 -5.4; 106 -5.7; 116 -5.8; 128 -6.0; 141 -5.9; 155 -5.9; 170 -5.7; 187 -5.3; 206 -4.6; 227 -4.7; 249 -5.1; 274 -5.3; 302 -5.2; 332 -5.3; 365 -5.2; 402 -5.2; 442 -5.4; 486 -5.6; 535 -5.5; 588 -5.4; 647 -5.2; 712 -5.1; 783 -5.1; 861 -5.1; 947 -5.3; 1042 -5.5; 1146 -5.9; 1261 -6.4; 1387 -6.7; 1526 -6.6; 1678 -6.5; 1846 -6.9; 2031 -7.4; 2234 -7.6; 2457 -7.2; 2703 -7.6; 2973 -8.1; 3270 -8.3; 3597 -8.0; 3957 -6.1; 4353 -3.5; 4788 -2.2; 5267 -2.2; 5793 -1.8; 6373 -0.5; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -7.0; 11289 -9.4; 12418 -9.3; 13660 -7.8; 15026 -6.9; 16529 -9.4; 18182 -12.5; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine (Cipher Cable) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine (Cipher Cable) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 1.11 | 2.8 dB  |
| Peaking | 3521 Hz  | 0.85 | -6.0 dB |
| Peaking | 5249 Hz  | 1.16 | 7.7 dB  |
| Peaking | 11566 Hz | 2.65 | -4.3 dB |
| Peaking | 19053 Hz | 0.77 | -8.4 dB |
| Peaking | 129 Hz   | 2.49 | -1.1 dB |
| Peaking | 2674 Hz  | 2.86 | 1.8 dB  |
| Peaking | 3052 Hz  | 1.17 | -1.3 dB |
| Peaking | 4405 Hz  | 6.88 | 1.5 dB  |
| Peaking | 9760 Hz  | 9.46 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -6.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Audeze%20Sine%20(Cipher%20Cable)/Audeze%20Sine%20(Cipher%20Cable).png)