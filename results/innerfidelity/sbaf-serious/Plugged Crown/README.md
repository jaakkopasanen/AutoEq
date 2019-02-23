# Plugged Crown
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.1; 25 -6.3; 28 -6.6; 31 -6.9; 34 -7.2; 37 -7.5; 41 -7.7; 45 -8.0; 49 -8.3; 54 -8.5; 60 -8.9; 66 -9.2; 72 -9.5; 79 -9.6; 87 -9.5; 96 -9.8; 106 -10.9; 116 -11.9; 128 -12.7; 141 -13.0; 155 -13.1; 170 -12.9; 187 -13.8; 206 -13.9; 227 -13.5; 249 -13.7; 274 -13.8; 302 -13.5; 332 -12.9; 365 -12.0; 402 -10.9; 442 -9.1; 486 -8.4; 535 -6.9; 588 -4.9; 647 -3.6; 712 -3.3; 783 -3.9; 861 -5.2; 947 -6.3; 1042 -6.7; 1146 -7.4; 1261 -7.7; 1387 -7.8; 1526 -7.7; 1678 -8.4; 1846 -8.8; 2031 -8.2; 2234 -7.1; 2457 -5.7; 2703 -4.7; 2973 -3.1; 3270 -1.9; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plugged Crown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plugged Crown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 142 Hz  | 0.6  | -3.1 dB |
| Peaking | 282 Hz  | 0.62 | -5.8 dB |
| Peaking | 667 Hz  | 1.84 | 6.2 dB  |
| Peaking | 1834 Hz | 1.51 | -3.3 dB |
| Peaking | 4317 Hz | 1.11 | 7.2 dB  |
| Peaking | 15 Hz   | 1.07 | 1.6 dB  |
| Peaking | 47 Hz   | 2.08 | -0.6 dB |
| Peaking | 6305 Hz | 3.5  | 3.8 dB  |
| Peaking | 7484 Hz | 3.11 | -1.5 dB |
| Peaking | 7852 Hz | 1.02 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -8.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Plugged%20Crown/Plugged%20Crown.png)