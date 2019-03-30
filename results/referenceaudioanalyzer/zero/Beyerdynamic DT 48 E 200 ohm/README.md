# Beyerdynamic DT 48 E 200 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -1.4; 249 -3.1; 274 -4.8; 302 -6.6; 332 -8.3; 365 -10.0; 402 -11.3; 442 -11.8; 486 -12.2; 535 -13.2; 588 -14.5; 647 -15.2; 712 -14.9; 783 -13.5; 861 -12.0; 947 -10.5; 1042 -9.3; 1146 -8.6; 1261 -8.4; 1387 -8.5; 1526 -9.1; 1678 -10.1; 1846 -11.3; 2031 -12.4; 2234 -13.0; 2457 -12.6; 2703 -11.1; 2973 -8.8; 3270 -6.3; 3597 -4.6; 3957 -3.7; 4353 -1.8; 4788 -0.5; 5267 -0.5; 5793 -1.8; 6373 -3.6; 7010 -5.8; 7711 -10.3; 8482 -14.8; 9330 -17.3; 10263 -16.0; 11289 -12.7; 12418 -12.5; 13660 -16.1; 15026 -18.3; 16529 -16.8; 18182 -13.3; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 E 200 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 E 200 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 645 Hz   | 1.92 | -9.4 dB  |
| Peaking | 2326 Hz  | 1.65 | -8.0 dB  |
| Peaking | 5186 Hz  | 1.08 | 8.8 dB   |
| Peaking | 9104 Hz  | 2.33 | -10.9 dB |
| Peaking | 15788 Hz | 0.83 | -11.7 dB |
| Peaking | 85 Hz    | 0.13 | 6.6 dB   |
| Peaking | 396 Hz   | 1.83 | -7.4 dB  |
| Peaking | 842 Hz   | 1.56 | -2.4 dB  |
| Peaking | 11964 Hz | 4.16 | 3.3 dB   |
| Peaking | 12606 Hz | 1.46 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.1 dB   |
| Peaking | 125 Hz   | 1.41 | 5.5 dB   |
| Peaking | 250 Hz   | 1.41 | 4.7 dB   |
| Peaking | 500 Hz   | 1.41 | -9.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 16000 Hz | 1.41 | -15.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%2048%20E%20200%20ohm/Beyerdynamic%20DT%2048%20E%20200%20ohm.png)