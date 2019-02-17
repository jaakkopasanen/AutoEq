# Beyerdynamic T1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.5; 25 -2.0; 28 -2.6; 31 -3.0; 34 -3.3; 37 -3.6; 41 -4.0; 45 -4.3; 49 -4.5; 54 -4.5; 60 -4.2; 66 -4.7; 72 -5.6; 79 -6.2; 87 -6.7; 96 -7.2; 106 -7.5; 116 -7.7; 128 -8.0; 141 -8.3; 155 -8.4; 170 -8.6; 187 -8.6; 206 -8.7; 227 -8.6; 249 -8.6; 274 -8.5; 302 -8.4; 332 -8.2; 365 -8.1; 402 -7.8; 442 -7.6; 486 -7.4; 535 -7.3; 588 -6.9; 647 -6.6; 712 -6.4; 783 -6.1; 861 -6.4; 947 -6.3; 1042 -6.0; 1146 -5.5; 1261 -5.7; 1387 -5.8; 1526 -6.3; 1678 -7.1; 1846 -7.6; 2031 -6.6; 2234 -6.1; 2457 -7.1; 2703 -6.8; 2973 -6.2; 3270 -5.1; 3597 -5.5; 3957 -6.2; 4353 -7.2; 4788 -4.5; 5267 -0.5; 5793 -8.3; 6373 -11.0; 7010 -6.7; 7711 -12.3; 8482 -16.5; 9330 -14.5; 10263 -8.3; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 15 Hz    |  0.56 | 5.8 dB   |
| Peaking | 61 Hz    |  3.49 | 1.5 dB   |
| Peaking | 197 Hz   |  0.56 | -2.8 dB  |
| Peaking | 5154 Hz  | 11.25 | 7.5 dB   |
| Peaking | 8594 Hz  |  3.43 | -11.3 dB |
| Peaking | 1815 Hz  |  3.15 | -3.7 dB  |
| Peaking | 2025 Hz  |  1.12 | 2.7 dB   |
| Peaking | 2533 Hz  |  3.75 | -2.4 dB  |
| Peaking | 6143 Hz  | 13.31 | -5.3 dB  |
| Peaking | 11186 Hz |  5.22 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1/Beyerdynamic%20T1.png)