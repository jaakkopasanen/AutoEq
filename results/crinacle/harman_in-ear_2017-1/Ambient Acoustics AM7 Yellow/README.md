# Ambient Acoustics AM7 Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.0; 41 -1.4; 45 -1.7; 49 -2.0; 54 -2.4; 60 -2.8; 66 -3.2; 72 -3.6; 79 -4.0; 87 -4.5; 96 -4.9; 106 -5.4; 116 -5.8; 128 -6.1; 141 -6.4; 155 -6.6; 170 -6.7; 187 -6.8; 206 -6.9; 227 -6.9; 249 -6.8; 274 -6.7; 302 -6.5; 332 -6.3; 365 -6.1; 402 -6.0; 442 -6.0; 486 -6.0; 535 -6.1; 588 -6.3; 647 -6.5; 712 -6.7; 783 -6.8; 861 -7.1; 947 -7.6; 1042 -8.3; 1146 -9.4; 1261 -10.6; 1387 -11.6; 1526 -12.7; 1678 -14.3; 1846 -15.6; 2031 -15.0; 2234 -11.3; 2457 -7.6; 2703 -5.9; 2973 -7.1; 3270 -9.4; 3597 -4.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.0; 5793 -1.4; 6373 -3.1; 7010 -6.1; 7711 -6.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -15.9; 16529 -27.5; 18182 -33.6; 20000 -24.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM7 Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM7 Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.62 | 6.3 dB   |
| Peaking | 1345 Hz  | 1.75 | -3.5 dB  |
| Peaking | 1908 Hz  | 2.08 | -11.2 dB |
| Peaking | 10801 Hz | 0.22 | 17.7 dB  |
| Peaking | 17999 Hz | 0.42 | -40.2 dB |
| Peaking | 3293 Hz  | 6.11 | -7.6 dB  |
| Peaking | 4414 Hz  | 1.25 | 4.3 dB   |
| Peaking | 7739 Hz  | 1.83 | -4.5 dB  |
| Peaking | 13785 Hz | 2.65 | 6.8 dB   |
| Peaking | 16292 Hz | 2.56 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 2.6 dB   |
| Peaking | 125 Hz   | 1.41 | -0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -21.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ambient%20Acoustics%20AM7%20Yellow/Ambient%20Acoustics%20AM7%20Yellow.png)