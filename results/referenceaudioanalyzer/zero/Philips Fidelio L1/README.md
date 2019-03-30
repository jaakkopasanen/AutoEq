# Philips Fidelio L1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.4; 23 -15.4; 25 -15.5; 28 -15.4; 31 -15.3; 34 -15.2; 37 -14.9; 41 -14.6; 45 -14.2; 49 -13.9; 54 -13.6; 60 -13.4; 66 -13.1; 72 -12.8; 79 -12.3; 87 -12.2; 96 -12.2; 106 -12.2; 116 -12.2; 128 -12.2; 141 -12.1; 155 -11.7; 170 -11.3; 187 -10.6; 206 -10.1; 227 -9.5; 249 -9.0; 274 -8.6; 302 -8.0; 332 -7.5; 365 -6.7; 402 -5.9; 442 -5.3; 486 -4.6; 535 -3.9; 588 -3.3; 647 -2.7; 712 -2.0; 783 -1.4; 861 -0.9; 947 -0.7; 1042 -0.5; 1146 -0.5; 1261 -0.6; 1387 -0.9; 1526 -1.4; 1678 -2.1; 1846 -2.7; 2031 -3.3; 2234 -4.3; 2457 -6.2; 2703 -9.6; 2973 -12.3; 3270 -12.8; 3597 -11.6; 3957 -10.4; 4353 -9.7; 4788 -9.6; 5267 -9.6; 5793 -8.8; 6373 -9.2; 7010 -10.3; 7711 -8.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio L1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio L1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.44 | -8.6 dB  |
| Peaking | 159 Hz  | 0.49 | -4.5 dB  |
| Peaking | 1275 Hz | 0.41 | 7.1 dB   |
| Peaking | 3199 Hz | 1.72 | -10.0 dB |
| Peaking | 6315 Hz | 1.76 | -3.3 dB  |
| Peaking | 1687 Hz | 3.8  | -0.6 dB  |
| Peaking | 2422 Hz | 3.11 | 1.0 dB   |
| Peaking | 2785 Hz | 5.99 | -1.2 dB  |
| Peaking | 7341 Hz | 6.02 | -3.0 dB  |
| Peaking | 7939 Hz | 2.54 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.4 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20Fidelio%20L1/Philips%20Fidelio%20L1.png)