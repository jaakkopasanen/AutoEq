# Sony XBA-Z5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.4; 25 -9.6; 28 -9.7; 31 -9.9; 34 -10.0; 37 -10.1; 41 -10.2; 45 -10.4; 49 -10.5; 54 -10.7; 60 -11.0; 66 -11.3; 72 -11.5; 79 -11.8; 87 -12.2; 96 -12.5; 106 -12.6; 116 -12.6; 128 -12.7; 141 -12.8; 155 -12.7; 170 -12.6; 187 -12.3; 206 -12.0; 227 -11.6; 249 -11.2; 274 -10.7; 302 -10.1; 332 -9.6; 365 -8.9; 402 -8.6; 442 -8.0; 486 -7.7; 535 -7.2; 588 -6.5; 647 -6.0; 712 -5.4; 783 -5.1; 861 -5.2; 947 -5.5; 1042 -5.7; 1146 -5.8; 1261 -5.9; 1387 -6.2; 1526 -6.3; 1678 -6.2; 1846 -5.5; 2031 -4.6; 2234 -3.9; 2457 -3.2; 2703 -2.2; 2973 -1.7; 3270 -0.5; 3597 -0.7; 3957 -3.3; 4353 -5.9; 4788 -6.4; 5267 -4.0; 5793 -0.7; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.6; 10263 -10.1; 11289 -10.2; 12418 -7.8; 13660 -7.7; 15026 -6.8; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-Z5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-Z5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 59 Hz    | 0.36 | -4.0 dB |
| Peaking | 173 Hz   | 0.8  | -4.3 dB |
| Peaking | 3113 Hz  | 2.02 | 5.8 dB  |
| Peaking | 6164 Hz  | 4.76 | 6.2 dB  |
| Peaking | 10920 Hz | 3.14 | -4.6 dB |
| Peaking | 15 Hz    | 1.75 | -1.0 dB |
| Peaking | 788 Hz   | 2.72 | 1.9 dB  |
| Peaking | 2157 Hz  | 8.1  | 0.4 dB  |
| Peaking | 4508 Hz  | 2.1  | 2.2 dB  |
| Peaking | 4584 Hz  | 4.57 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20XBA-Z5/Sony%20XBA-Z5.png)