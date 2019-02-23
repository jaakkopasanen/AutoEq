# Philips Construct
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.2; 25 -12.2; 28 -12.3; 31 -12.3; 34 -12.2; 37 -12.2; 41 -12.1; 45 -11.9; 49 -11.7; 54 -11.5; 60 -11.1; 66 -10.9; 72 -11.1; 79 -11.9; 87 -12.9; 96 -13.5; 106 -13.2; 116 -13.3; 128 -13.4; 141 -13.0; 155 -12.2; 170 -11.6; 187 -11.0; 206 -10.0; 227 -8.8; 249 -7.6; 274 -6.4; 302 -5.7; 332 -5.8; 365 -6.5; 402 -8.0; 442 -9.3; 486 -10.6; 535 -11.5; 588 -11.8; 647 -12.1; 712 -12.3; 783 -11.9; 861 -11.8; 947 -11.5; 1042 -10.6; 1146 -9.6; 1261 -8.5; 1387 -7.8; 1526 -7.2; 1678 -6.4; 1846 -5.2; 2031 -3.7; 2234 -2.3; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.5; 4788 -2.5; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Construct GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Construct ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.46 | -5.7 dB |
| Peaking | 121 Hz  | 1.32 | -6.0 dB |
| Peaking | 789 Hz  | 1.15 | -6.4 dB |
| Peaking | 2993 Hz | 1.23 | 6.9 dB  |
| Peaking | 5799 Hz | 3.36 | 5.1 dB  |
| Peaking | 192 Hz  | 2.99 | -1.7 dB |
| Peaking | 314 Hz  | 2.03 | 3.1 dB  |
| Peaking | 507 Hz  | 3.23 | -2.0 dB |
| Peaking | 8342 Hz | 3.89 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -5.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Construct/Philips%20Construct.png)