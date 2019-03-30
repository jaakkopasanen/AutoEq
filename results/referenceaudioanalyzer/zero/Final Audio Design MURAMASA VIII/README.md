# Final Audio Design MURAMASA VIII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.9; 206 -1.4; 227 -1.7; 249 -1.7; 274 -1.5; 302 -1.3; 332 -0.9; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -2.7; 647 -6.5; 712 -9.2; 783 -10.4; 861 -10.4; 947 -10.2; 1042 -10.4; 1146 -11.0; 1261 -12.1; 1387 -13.4; 1526 -14.8; 1678 -15.9; 1846 -15.7; 2031 -13.8; 2234 -11.0; 2457 -8.7; 2703 -7.6; 2973 -8.7; 3270 -11.6; 3597 -14.2; 3957 -14.5; 4353 -13.5; 4788 -12.4; 5267 -11.5; 5793 -8.6; 6373 -6.7; 7010 -8.4; 7711 -9.5; 8482 -8.8; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -7.4; 13660 -7.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Design MURAMASA VIII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Design MURAMASA VIII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.08 | 6.1 dB  |
| Peaking | 535 Hz   | 1.54 | 8.2 dB  |
| Peaking | 739 Hz   | 1.19 | -8.9 dB |
| Peaking | 1680 Hz  | 2.25 | -9.1 dB |
| Peaking | 4149 Hz  | 2.13 | -7.8 dB |
| Peaking | 2044 Hz  | 4.98 | -2.3 dB |
| Peaking | 2786 Hz  | 2.11 | 2.9 dB  |
| Peaking | 3446 Hz  | 5.29 | -3.1 dB |
| Peaking | 7929 Hz  | 6.2  | -2.7 dB |
| Peaking | 20778 Hz | 2.43 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.8 dB  |
| Peaking | 250 Hz   | 1.41 | 3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 6.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | -5.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Final%20Audio%20Design%20MURAMASA%20VIII/Final%20Audio%20Design%20MURAMASA%20VIII.png)