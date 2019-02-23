# Audeze LCD-XC sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -2.8; 25 -2.7; 28 -2.5; 31 -2.6; 34 -2.9; 37 -3.2; 41 -3.3; 45 -3.3; 49 -3.4; 54 -3.8; 60 -4.3; 66 -4.7; 72 -5.0; 79 -5.3; 87 -5.6; 96 -5.8; 106 -6.1; 116 -6.2; 128 -6.3; 141 -6.5; 155 -6.4; 170 -6.5; 187 -6.5; 206 -6.4; 227 -5.9; 249 -5.5; 274 -4.9; 302 -4.6; 332 -4.3; 365 -3.7; 402 -3.3; 442 -3.2; 486 -3.4; 535 -3.2; 588 -3.0; 647 -2.9; 712 -3.3; 783 -3.6; 861 -4.3; 947 -5.0; 1042 -5.6; 1146 -6.2; 1261 -7.0; 1387 -8.2; 1526 -9.1; 1678 -9.5; 1846 -9.2; 2031 -8.0; 2234 -6.3; 2457 -4.8; 2703 -3.4; 2973 -2.9; 3270 -2.9; 3597 -5.0; 3957 -6.5; 4353 -3.6; 4788 -0.8; 5267 -0.6; 5793 -0.5; 6373 -0.7; 7010 -2.0; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -8.4; 15026 -7.9; 16529 -7.7; 18182 -10.3; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1    | 2.0 dB  |
| Peaking | 139 Hz   | 1.26 | -2.3 dB |
| Peaking | 1658 Hz  | 2.55 | -5.7 dB |
| Peaking | 5795 Hz  | 2.14 | 4.8 dB  |
| Peaking | 18964 Hz | 0.5  | -5.9 dB |
| Peaking | 557 Hz   | 1.71 | 1.9 dB  |
| Peaking | 3006 Hz  | 4.63 | 2.2 dB  |
| Peaking | 4001 Hz  | 8.72 | -3.6 dB |
| Peaking | 12336 Hz | 2.78 | 2.0 dB  |
| Peaking | 13788 Hz | 4.38 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC%20sample%201/Audeze%20LCD-XC%20sample%201.png)