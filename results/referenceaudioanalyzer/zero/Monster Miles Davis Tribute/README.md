# Monster Miles Davis Tribute
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.1; 23 -17.2; 25 -17.3; 28 -17.4; 31 -17.6; 34 -17.6; 37 -17.6; 41 -17.5; 45 -17.4; 49 -17.2; 54 -17.0; 60 -16.7; 66 -16.5; 72 -16.4; 79 -16.1; 87 -15.8; 96 -15.3; 106 -14.9; 116 -14.4; 128 -13.7; 141 -13.5; 155 -13.5; 170 -13.1; 187 -12.3; 206 -11.6; 227 -10.9; 249 -10.3; 274 -9.6; 302 -8.9; 332 -8.3; 365 -7.6; 402 -6.8; 442 -6.1; 486 -5.4; 535 -4.7; 588 -4.0; 647 -3.4; 712 -2.7; 783 -2.2; 861 -1.7; 947 -1.3; 1042 -1.1; 1146 -0.9; 1261 -0.8; 1387 -0.6; 1526 -0.5; 1678 -0.5; 1846 -0.9; 2031 -1.7; 2234 -2.7; 2457 -3.8; 2703 -5.2; 2973 -6.6; 3270 -7.0; 3597 -6.6; 3957 -6.1; 4353 -6.1; 4788 -6.4; 5267 -6.2; 5793 -4.6; 6373 -1.6; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Miles Davis Tribute GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Miles Davis Tribute ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.11 | -11.8 dB |
| Peaking | 1496 Hz | 0.4  | 6.1 dB   |
| Peaking | 3063 Hz | 1.9  | -4.6 dB  |
| Peaking | 5588 Hz | 1.09 | -3.0 dB  |
| Peaking | 6504 Hz | 4.58 | 6.1 dB   |
| Peaking | 39 Hz   | 2.18 | -0.3 dB  |
| Peaking | 132 Hz  | 2.8  | 0.8 dB   |
| Peaking | 162 Hz  | 3.19 | -0.7 dB  |
| Peaking | 729 Hz  | 3.83 | 0.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.6 dB |
| Peaking | 62 Hz    | 1.41 | -8.1 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monster%20Miles%20Davis%20Tribute/Monster%20Miles%20Davis%20Tribute.png)