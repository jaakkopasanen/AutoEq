# Phonon SMB2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -3.0; 25 -3.8; 28 -4.8; 31 -5.7; 34 -6.4; 37 -7.0; 41 -7.6; 45 -8.1; 49 -8.4; 54 -8.7; 60 -9.1; 66 -9.3; 72 -9.4; 79 -9.5; 87 -9.5; 96 -9.7; 106 -9.7; 116 -9.5; 128 -9.6; 141 -9.9; 155 -10.0; 170 -9.7; 187 -9.8; 206 -9.7; 227 -9.6; 249 -9.9; 274 -9.7; 302 -9.4; 332 -8.9; 365 -8.2; 402 -7.4; 442 -6.5; 486 -6.3; 535 -5.9; 588 -5.3; 647 -5.7; 712 -6.3; 783 -6.7; 861 -7.3; 947 -7.7; 1042 -7.9; 1146 -8.1; 1261 -8.1; 1387 -8.9; 1526 -9.7; 1678 -10.3; 1846 -10.2; 2031 -9.3; 2234 -7.9; 2457 -5.6; 2703 -4.3; 2973 -2.4; 3270 -1.7; 3597 -3.0; 3957 -1.9; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -1.8; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -8.0; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phonon SMB2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phonon SMB2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.82 | 5.0 dB  |
| Peaking | 124 Hz  | 0.48 | -3.6 dB |
| Peaking | 1788 Hz | 1.85 | -4.7 dB |
| Peaking | 3102 Hz | 2.19 | 4.3 dB  |
| Peaking | 5080 Hz | 2.1  | 6.1 dB  |
| Peaking | 50 Hz   | 2.49 | -0.6 dB |
| Peaking | 281 Hz  | 2.78 | -1.4 dB |
| Peaking | 566 Hz  | 2.63 | 2.0 dB  |
| Peaking | 6577 Hz | 7.55 | 1.6 dB  |
| Peaking | 9157 Hz | 3.24 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phonon%20SMB2/Phonon%20SMB2.png)