# Audeze EL8 Closed
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.6; 28 -5.7; 31 -5.7; 34 -5.6; 37 -5.5; 41 -5.5; 45 -5.4; 49 -5.0; 54 -4.7; 60 -5.9; 66 -7.0; 72 -7.3; 79 -7.7; 87 -8.0; 96 -8.5; 106 -8.7; 116 -8.6; 128 -8.3; 141 -7.5; 155 -6.7; 170 -6.3; 187 -5.8; 206 -5.1; 227 -4.6; 249 -4.4; 274 -4.2; 302 -4.3; 332 -4.5; 365 -4.5; 402 -4.8; 442 -5.1; 486 -5.4; 535 -5.5; 588 -5.5; 647 -6.0; 712 -6.6; 783 -6.8; 861 -7.2; 947 -7.5; 1042 -7.7; 1146 -7.8; 1261 -8.3; 1387 -8.8; 1526 -9.6; 1678 -10.2; 1846 -10.3; 2031 -9.7; 2234 -8.9; 2457 -7.9; 2703 -7.7; 2973 -8.4; 3270 -8.9; 3597 -9.4; 3957 -9.2; 4353 -10.4; 4788 -12.2; 5267 -5.9; 5793 -0.5; 6373 -0.8; 7010 -3.7; 7711 -5.9; 8482 -6.5; 9330 -8.8; 10263 -6.3; 11289 -6.2; 12418 -6.2; 13660 -7.0; 15026 -10.5; 16529 -9.2; 18182 -7.8; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze EL8 Closed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze EL8 Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 105 Hz   | 2.86 | -2.9 dB |
| Peaking | 1731 Hz  | 1.66 | -4.0 dB |
| Peaking | 4849 Hz  | 2.28 | -9.1 dB |
| Peaking | 5856 Hz  | 2.97 | 11.5 dB |
| Peaking | 19504 Hz | 0.25 | -3.0 dB |
| Peaking | 51 Hz    | 4.72 | 1.6 dB  |
| Peaking | 304 Hz   | 1.47 | 2.3 dB  |
| Peaking | 9203 Hz  | 5.58 | -3.1 dB |
| Peaking | 14472 Hz | 0.81 | 3.2 dB  |
| Peaking | 15272 Hz | 2.36 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20EL8%20Closed/Audeze%20EL8%20Closed.png)