# Piaton Moderna MS200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.5; 25 -3.1; 28 -3.9; 31 -4.6; 34 -5.2; 37 -5.7; 41 -6.4; 45 -7.0; 49 -7.5; 54 -8.0; 60 -8.7; 66 -9.3; 72 -9.8; 79 -10.4; 87 -10.9; 96 -11.6; 106 -11.9; 116 -12.1; 128 -12.4; 141 -12.7; 155 -12.9; 170 -12.9; 187 -13.0; 206 -12.9; 227 -12.7; 249 -12.5; 274 -12.3; 302 -11.9; 332 -11.5; 365 -11.0; 402 -10.2; 442 -9.2; 486 -9.4; 535 -8.9; 588 -7.8; 647 -6.7; 712 -5.8; 783 -4.7; 861 -3.8; 947 -3.2; 1042 -2.7; 1146 -2.5; 1261 -2.5; 1387 -3.4; 1526 -4.7; 1678 -5.4; 1846 -6.1; 2031 -6.4; 2234 -6.4; 2457 -4.8; 2703 -2.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.1; 5267 -0.6; 5793 -1.1; 6373 -3.8; 7010 -5.4; 7711 -6.3; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Piaton Moderna MS200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton Moderna MS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.87 | 5.4 dB  |
| Peaking | 94 Hz   | 0.84 | -1.9 dB |
| Peaking | 214 Hz  | 0.5  | -6.0 dB |
| Peaking | 1015 Hz | 1.64 | 4.9 dB  |
| Peaking | 4092 Hz | 1.31 | 6.8 dB  |
| Peaking | 2185 Hz | 3.46 | -2.5 dB |
| Peaking | 2948 Hz | 3.81 | 2.8 dB  |
| Peaking | 4149 Hz | 2.72 | -1.2 dB |
| Peaking | 5653 Hz | 4.26 | 3.0 dB  |
| Peaking | 7754 Hz | 1.51 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Piaton%20Moderna%20MS200/Piaton%20Moderna%20MS200.png)