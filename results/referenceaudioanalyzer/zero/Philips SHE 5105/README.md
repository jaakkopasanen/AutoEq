# Philips SHE 5105
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.9; 25 -12.4; 28 -12.9; 31 -13.4; 34 -13.7; 37 -14.0; 41 -14.2; 45 -14.4; 49 -14.5; 54 -14.6; 60 -14.6; 66 -14.4; 72 -14.3; 79 -14.2; 87 -14.0; 96 -13.7; 106 -13.4; 116 -13.1; 128 -12.7; 141 -12.3; 155 -11.8; 170 -11.3; 187 -10.7; 206 -10.1; 227 -9.4; 249 -8.7; 274 -7.9; 302 -7.3; 332 -7.2; 365 -6.9; 402 -6.4; 442 -5.5; 486 -4.8; 535 -4.0; 588 -3.3; 647 -2.7; 712 -2.1; 783 -1.5; 861 -1.0; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -1.5; 2457 -3.3; 2703 -6.3; 2973 -10.5; 3270 -13.5; 3597 -14.2; 3957 -12.8; 4353 -11.4; 4788 -12.0; 5267 -14.4; 5793 -15.0; 6373 -12.2; 7010 -6.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHE 5105 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE 5105 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.58 | -3.1 dB  |
| Peaking | 84 Hz   | 0.37 | -6.7 dB  |
| Peaking | 1893 Hz | 0.35 | 8.5 dB   |
| Peaking | 3426 Hz | 1.93 | -14.0 dB |
| Peaking | 5626 Hz | 2.93 | -10.5 dB |
| Peaking | 1460 Hz | 3.6  | -0.8 dB  |
| Peaking | 2209 Hz | 3.9  | 1.3 dB   |
| Peaking | 6216 Hz | 5.76 | -1.5 dB  |
| Peaking | 7136 Hz | 6.34 | 3.6 dB   |
| Peaking | 8547 Hz | 0.4  | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -6.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHE%205105/Philips%20SHE%205105.png)