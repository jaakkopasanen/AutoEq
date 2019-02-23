# Audeze LCD-XC sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.3; 25 -1.2; 28 -1.0; 31 -0.9; 34 -1.0; 37 -1.3; 41 -1.6; 45 -1.6; 49 -1.7; 54 -2.2; 60 -3.8; 66 -5.1; 72 -5.3; 79 -5.5; 87 -5.8; 96 -6.0; 106 -5.9; 116 -6.1; 128 -6.3; 141 -6.3; 155 -6.1; 170 -6.4; 187 -6.4; 206 -6.3; 227 -6.0; 249 -5.8; 274 -5.6; 302 -5.5; 332 -5.4; 365 -5.4; 402 -5.6; 442 -5.6; 486 -6.1; 535 -6.1; 588 -5.7; 647 -5.8; 712 -6.4; 783 -6.8; 861 -7.4; 947 -7.7; 1042 -8.2; 1146 -9.0; 1261 -9.7; 1387 -10.6; 1526 -11.6; 1678 -12.2; 1846 -12.0; 2031 -10.9; 2234 -9.3; 2457 -7.3; 2703 -6.0; 2973 -5.0; 3270 -4.0; 3597 -3.4; 3957 -5.2; 4353 -9.3; 4788 -11.3; 5267 -4.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.8; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -8.2; 16529 -8.5; 18182 -10.1; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 31 Hz    |  0.82 | 6.0 dB   |
| Peaking | 1717 Hz  |  1.69 | -6.4 dB  |
| Peaking | 3565 Hz  |  1.97 | 5.2 dB   |
| Peaking | 4733 Hz  |  3.43 | -10.3 dB |
| Peaking | 5735 Hz  |  3.32 | 9.5 dB   |
| Peaking | 51 Hz    |  3.59 | 2.2 dB   |
| Peaking | 66 Hz    |  0.69 | -0.9 dB  |
| Peaking | 374 Hz   |  1.17 | 1.2 dB   |
| Peaking | 6562 Hz  | 13.28 | 1.7 dB   |
| Peaking | 19941 Hz |  0.52 | -5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC%20sample%202/Audeze%20LCD-XC%20sample%202.png)