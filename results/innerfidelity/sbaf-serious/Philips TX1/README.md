# Philips TX1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.5; 25 -13.4; 28 -13.3; 31 -13.3; 34 -13.2; 37 -13.1; 41 -13.0; 45 -12.9; 49 -12.9; 54 -12.8; 60 -12.8; 66 -12.8; 72 -12.7; 79 -12.8; 87 -12.8; 96 -12.8; 106 -12.5; 116 -12.3; 128 -12.1; 141 -11.9; 155 -11.6; 170 -11.2; 187 -10.8; 206 -10.3; 227 -9.8; 249 -9.3; 274 -8.7; 302 -8.2; 332 -7.6; 365 -7.1; 402 -6.6; 442 -6.0; 486 -5.5; 535 -5.0; 588 -4.4; 647 -4.1; 712 -4.1; 783 -3.7; 861 -3.9; 947 -4.2; 1042 -4.6; 1146 -4.9; 1261 -5.3; 1387 -6.1; 1526 -6.8; 1678 -7.3; 1846 -7.3; 2031 -7.0; 2234 -6.3; 2457 -4.7; 2703 -3.4; 2973 -1.5; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -5.1; 4788 -7.6; 5267 -8.5; 5793 -7.2; 6373 -5.4; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips TX1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips TX1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.26 | -6.6 dB |
| Peaking | 130 Hz  | 0.6  | -4.0 dB |
| Peaking | 698 Hz  | 1.3  | 3.3 dB  |
| Peaking | 3464 Hz | 2.57 | 6.9 dB  |
| Peaking | 5064 Hz | 5.16 | -3.7 dB |
| Peaking | 1187 Hz | 1.6  | 1.7 dB  |
| Peaking | 1834 Hz | 1.01 | -2.5 dB |
| Peaking | 2705 Hz | 2.75 | 2.1 dB  |
| Peaking | 6874 Hz | 7.75 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20TX1/Philips%20TX1.png)