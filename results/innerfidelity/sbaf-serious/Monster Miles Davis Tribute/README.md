# Monster Miles Davis Tribute
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.2; 25 -13.2; 28 -13.1; 31 -12.9; 34 -12.8; 37 -12.7; 41 -12.6; 45 -12.4; 49 -12.3; 54 -12.2; 60 -12.1; 66 -12.1; 72 -12.0; 79 -11.9; 87 -11.9; 96 -11.8; 106 -11.6; 116 -11.3; 128 -11.2; 141 -10.9; 155 -10.6; 170 -10.1; 187 -9.8; 206 -9.3; 227 -8.7; 249 -8.3; 274 -7.9; 302 -7.4; 332 -6.8; 365 -6.2; 402 -5.8; 442 -5.1; 486 -4.8; 535 -4.3; 588 -3.6; 647 -3.3; 712 -3.2; 783 -3.0; 861 -3.2; 947 -3.6; 1042 -4.1; 1146 -4.6; 1261 -5.1; 1387 -6.0; 1526 -7.1; 1678 -8.0; 1846 -8.7; 2031 -9.2; 2234 -9.8; 2457 -9.2; 2703 -8.6; 2973 -5.3; 3270 -2.5; 3597 -1.2; 3957 -2.4; 4353 -5.1; 4788 -6.4; 5267 -4.7; 5793 -2.0; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Miles Davis Tribute GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Miles Davis Tribute ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.34 | -7.2 dB |
| Peaking | 130 Hz  | 1.06 | -3.4 dB |
| Peaking | 2291 Hz | 2.65 | -4.7 dB |
| Peaking | 3536 Hz | 4.2  | 5.8 dB  |
| Peaking | 6282 Hz | 5.3  | 5.9 dB  |
| Peaking | 133 Hz  | 2.08 | 1.3 dB  |
| Peaking | 213 Hz  | 0.6  | -1.3 dB |
| Peaking | 734 Hz  | 0.85 | 3.5 dB  |
| Peaking | 1679 Hz | 2.78 | -2.0 dB |
| Peaking | 4700 Hz | 9.88 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Miles%20Davis%20Tribute/Monster%20Miles%20Davis%20Tribute.png)