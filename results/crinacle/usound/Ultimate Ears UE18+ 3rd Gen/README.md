# Ultimate Ears UE18+ 3rd Gen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.7; 25 -3.0; 28 -3.4; 31 -3.8; 34 -4.1; 37 -4.4; 41 -4.7; 45 -4.9; 49 -5.2; 54 -5.5; 60 -5.9; 66 -6.3; 72 -6.7; 79 -7.1; 87 -7.6; 96 -8.1; 106 -8.6; 116 -9.0; 128 -9.3; 141 -9.8; 155 -10.1; 170 -10.3; 187 -10.5; 206 -10.6; 227 -10.7; 249 -10.8; 274 -10.8; 302 -10.9; 332 -10.9; 365 -10.9; 402 -11.0; 442 -11.1; 486 -11.1; 535 -11.1; 588 -11.1; 647 -10.9; 712 -10.4; 783 -9.6; 861 -8.5; 947 -7.3; 1042 -6.4; 1146 -6.0; 1261 -6.2; 1387 -6.5; 1526 -6.4; 1678 -5.6; 1846 -4.3; 2031 -3.1; 2234 -2.4; 2457 -2.4; 2703 -2.6; 2973 -2.0; 3270 -1.3; 3597 -1.9; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -3.4; 5793 -2.9; 6373 -2.4; 7010 -5.5; 7711 -7.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.4; 16529 -17.9; 18182 -15.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE18+ 3rd Gen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE18+ 3rd Gen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.34 | 4.5 dB   |
| Peaking | 325 Hz   | 0.36 | -5.0 dB  |
| Peaking | 3445 Hz  | 0.71 | 5.9 dB   |
| Peaking | 17116 Hz | 1.91 | -13.6 dB |
| Peaking | 659 Hz   | 3.03 | -1.2 dB  |
| Peaking | 1048 Hz  | 4.09 | 1.7 dB   |
| Peaking | 6575 Hz  | 4.58 | 3.2 dB   |
| Peaking | 7376 Hz  | 3.77 | -3.9 dB  |
| Peaking | 13859 Hz | 4.76 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -4.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -8.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20UE18+%203rd%20Gen/Ultimate%20Ears%20UE18+%203rd%20Gen.png)