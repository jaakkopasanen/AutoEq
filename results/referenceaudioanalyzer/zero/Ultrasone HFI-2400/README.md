# Ultrasone HFI-2400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -1.8; 37 -2.7; 41 -3.6; 45 -4.2; 49 -4.6; 54 -5.1; 60 -5.7; 66 -6.2; 72 -6.5; 79 -6.8; 87 -6.8; 96 -6.5; 106 -6.3; 116 -6.0; 128 -5.7; 141 -5.2; 155 -4.7; 170 -4.2; 187 -3.7; 206 -3.7; 227 -4.1; 249 -4.2; 274 -3.9; 302 -3.2; 332 -2.6; 365 -2.2; 402 -2.0; 442 -1.8; 486 -1.5; 535 -1.1; 588 -0.8; 647 -0.7; 712 -0.9; 783 -1.1; 861 -1.4; 947 -2.0; 1042 -2.9; 1146 -3.9; 1261 -4.8; 1387 -5.5; 1526 -5.8; 1678 -4.8; 1846 -2.4; 2031 -0.5; 2234 -0.5; 2457 -2.9; 2703 -5.6; 2973 -8.7; 3270 -11.7; 3597 -13.9; 3957 -15.3; 4353 -16.4; 4788 -17.8; 5267 -19.5; 5793 -21.0; 6373 -20.9; 7010 -18.4; 7711 -13.9; 8482 -11.1; 9330 -11.9; 10263 -13.9; 11289 -14.7; 12418 -14.9; 13660 -15.0; 15026 -14.2; 16529 -11.2; 18182 -7.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-2400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.32 | 6.6 dB   |
| Peaking | 575 Hz   | 0.63 | 5.9 dB   |
| Peaking | 2212 Hz  | 3.08 | 8.5 dB   |
| Peaking | 5490 Hz  | 1.08 | -14.2 dB |
| Peaking | 13942 Hz | 1.2  | -7.9 dB  |
| Peaking | 188 Hz   | 4.97 | 1.4 dB   |
| Peaking | 1455 Hz  | 6.01 | -1.6 dB  |
| Peaking | 6737 Hz  | 4.61 | -3.8 dB  |
| Peaking | 8501 Hz  | 1.96 | 4.1 dB   |
| Peaking | 10623 Hz | 2.84 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB   |
| Peaking | 250 Hz   | 1.41 | 1.8 dB   |
| Peaking | 500 Hz   | 1.41 | 5.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.8 dB |
| Peaking | 8000 Hz  | 1.41 | -9.1 dB  |
| Peaking | 16000 Hz | 1.41 | -7.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20HFI-2400/Ultrasone%20HFI-2400.png)