# Phonon SMB2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.5; 25 -2.3; 28 -3.4; 31 -4.2; 34 -5.0; 37 -5.6; 41 -6.2; 45 -6.7; 49 -7.0; 54 -7.3; 60 -7.6; 66 -7.8; 72 -7.9; 79 -8.0; 87 -8.1; 96 -8.2; 106 -8.3; 116 -8.1; 128 -8.2; 141 -8.5; 155 -8.6; 170 -8.3; 187 -8.3; 206 -8.3; 227 -8.2; 249 -8.5; 274 -8.3; 302 -7.9; 332 -7.5; 365 -6.8; 402 -6.0; 442 -5.1; 486 -4.9; 535 -4.5; 588 -3.9; 647 -4.2; 712 -4.9; 783 -5.2; 861 -5.8; 947 -6.3; 1042 -6.5; 1146 -6.6; 1261 -6.6; 1387 -7.5; 1526 -8.3; 1678 -8.9; 1846 -8.8; 2031 -7.9; 2234 -6.5; 2457 -4.2; 2703 -2.9; 2973 -1.0; 3270 -0.5; 3597 -1.6; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phonon SMB2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phonon SMB2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.17 | 6.6 dB  |
| Peaking | 198 Hz  | 0.22 | -2.3 dB |
| Peaking | 566 Hz  | 1.31 | 4.2 dB  |
| Peaking | 1813 Hz | 2.29 | -4.3 dB |
| Peaking | 4002 Hz | 0.9  | 6.9 dB  |
| Peaking | 120 Hz  | 5.92 | 0.3 dB  |
| Peaking | 3143 Hz | 4.32 | 1.8 dB  |
| Peaking | 3695 Hz | 4.4  | -1.9 dB |
| Peaking | 6304 Hz | 2.62 | 4.9 dB  |
| Peaking | 7324 Hz | 1.44 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phonon%20SMB2/Phonon%20SMB2.png)