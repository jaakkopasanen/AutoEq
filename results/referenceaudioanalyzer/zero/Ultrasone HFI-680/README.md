# Ultrasone HFI-680
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -2.7; 332 -5.1; 365 -7.2; 402 -9.1; 442 -10.4; 486 -11.1; 535 -11.1; 588 -10.8; 647 -10.3; 712 -9.8; 783 -9.5; 861 -9.3; 947 -9.5; 1042 -9.6; 1146 -9.4; 1261 -9.4; 1387 -9.9; 1526 -10.5; 1678 -10.0; 1846 -8.4; 2031 -6.8; 2234 -6.7; 2457 -7.6; 2703 -9.0; 2973 -10.4; 3270 -11.7; 3597 -12.2; 3957 -11.9; 4353 -11.2; 4788 -11.7; 5267 -13.2; 5793 -12.5; 6373 -9.3; 7010 -8.4; 7711 -9.4; 8482 -8.2; 9330 -6.6; 10263 -9.8; 11289 -16.1; 12418 -18.9; 13660 -15.7; 15026 -9.4; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-680 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 491 Hz   | 1.59 | -9.0 dB  |
| Peaking | 567 Hz   | 0.02 | 6.9 dB   |
| Peaking | 1140 Hz  | 0.71 | -8.2 dB  |
| Peaking | 4526 Hz  | 0.81 | -11.3 dB |
| Peaking | 12535 Hz | 1.96 | -16.7 dB |
| Peaking | 264 Hz   | 5.37 | 2.2 dB   |
| Peaking | 2151 Hz  | 1.59 | -3.2 dB  |
| Peaking | 2174 Hz  | 3.18 | 5.1 dB   |
| Peaking | 9505 Hz  | 6.6  | 3.0 dB   |
| Peaking | 11222 Hz | 7.51 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.6 dB  |
| Peaking | 250 Hz   | 1.41 | 6.4 dB  |
| Peaking | 500 Hz   | 1.41 | -5.8 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.6 dB |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -5.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20HFI-680/Ultrasone%20HFI-680.png)