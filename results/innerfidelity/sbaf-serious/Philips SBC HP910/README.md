# Philips SBC HP910
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.2; 49 -1.7; 54 -2.4; 60 -2.9; 66 -3.2; 72 -3.8; 79 -3.6; 87 -3.8; 96 -5.1; 106 -5.7; 116 -6.1; 128 -6.3; 141 -6.5; 155 -6.5; 170 -6.2; 187 -6.3; 206 -6.2; 227 -6.0; 249 -5.7; 274 -5.4; 302 -5.0; 332 -4.8; 365 -4.5; 402 -4.1; 442 -3.8; 486 -3.8; 535 -3.7; 588 -3.9; 647 -3.1; 712 -3.7; 783 -3.9; 861 -4.5; 947 -4.8; 1042 -5.2; 1146 -5.3; 1261 -5.6; 1387 -5.7; 1526 -5.8; 1678 -6.3; 1846 -6.8; 2031 -7.0; 2234 -8.2; 2457 -9.0; 2703 -10.0; 2973 -10.5; 3270 -9.1; 3597 -7.0; 3957 -6.0; 4353 -5.1; 4788 -9.1; 5267 -8.1; 5793 -4.8; 6373 -8.2; 7010 -11.6; 7711 -12.5; 8482 -13.5; 9330 -10.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SBC HP910 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SBC HP910 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.68 | 6.6 dB  |
| Peaking | 603 Hz   | 0.93 | 3.1 dB  |
| Peaking | 2801 Hz  | 3.46 | -4.3 dB |
| Peaking | 8326 Hz  | 2.68 | -8.2 dB |
| Peaking | 10337 Hz | 2.92 | 2.4 dB  |
| Peaking | 83 Hz    | 4.79 | 1.3 dB  |
| Peaking | 133 Hz   | 1.74 | -1.0 dB |
| Peaking | 4890 Hz  | 2.98 | 4.5 dB  |
| Peaking | 4927 Hz  | 7.61 | -7.4 dB |
| Peaking | 14521 Hz | 2.67 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SBC%20HP910/Philips%20SBC%20HP910.png)