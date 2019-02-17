# Monster Miles Davis Tribute
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.8; 25 -13.8; 28 -13.7; 31 -13.5; 34 -13.4; 37 -13.3; 41 -13.2; 45 -13.0; 49 -12.9; 54 -12.8; 60 -12.7; 66 -12.7; 72 -12.6; 79 -12.5; 87 -12.5; 96 -12.4; 106 -12.2; 116 -11.9; 128 -11.8; 141 -11.5; 155 -11.2; 170 -10.7; 187 -10.4; 206 -9.9; 227 -9.3; 249 -8.9; 274 -8.5; 302 -8.0; 332 -7.4; 365 -6.8; 402 -6.4; 442 -5.7; 486 -5.4; 535 -4.9; 588 -4.2; 647 -3.9; 712 -3.8; 783 -3.6; 861 -3.8; 947 -4.2; 1042 -4.7; 1146 -5.2; 1261 -5.7; 1387 -6.6; 1526 -7.7; 1678 -8.6; 1846 -9.3; 2031 -9.8; 2234 -10.4; 2457 -9.8; 2703 -9.2; 2973 -5.9; 3270 -3.1; 3597 -1.8; 3957 -3.0; 4353 -5.7; 4788 -7.0; 5267 -5.3; 5793 -2.6; 6373 -0.5; 7010 -1.9; 7711 -4.2; 8482 -4.4; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.7; 15026 -5.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Miles Davis Tribute GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Miles Davis Tribute ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.2  | -9.1 dB |
| Peaking | 157 Hz   | 0.8  | -3.6 dB |
| Peaking | 2269 Hz  | 1.53 | -6.4 dB |
| Peaking | 3472 Hz  | 4.82 | 5.3 dB  |
| Peaking | 6497 Hz  | 6.3  | 5.0 dB  |
| Peaking | 314 Hz   | 2.01 | -0.8 dB |
| Peaking | 756 Hz   | 1.34 | 1.8 dB  |
| Peaking | 1579 Hz  | 4.11 | -1.2 dB |
| Peaking | 4751 Hz  | 8.38 | -2.8 dB |
| Peaking | 14483 Hz | 6.66 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Miles%20Davis%20Tribute/Monster%20Miles%20Davis%20Tribute.png)