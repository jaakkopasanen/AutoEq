# Mee Audio Pinnacle PX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -0.2; 23 -0.6; 25 -0.9; 28 -1.2; 31 -1.6; 34 -1.8; 37 -2.0; 41 -2.3; 45 -2.6; 49 -2.8; 54 -3.2; 60 -3.5; 66 -3.8; 72 -4.1; 79 -4.5; 87 -4.9; 96 -5.2; 106 -5.5; 116 -5.8; 128 -5.9; 141 -5.9; 155 -5.9; 170 -7.2; 187 -7.4; 206 -7.1; 227 -6.7; 249 -6.4; 274 -6.0; 302 -5.6; 332 -5.2; 365 -5.0; 402 -4.7; 442 -4.2; 486 -3.6; 535 -3.0; 588 -2.5; 647 -1.9; 712 -1.3; 783 -0.7; 861 -0.2; 947 -0.0; 1042 -0.0; 1146 -0.3; 1261 -0.6; 1387 -0.4; 1526 -0.0; 1678 0.8; 1846 0.8; 2031 0.5; 2234 -0.3; 2457 -1.7; 2703 -3.3; 2973 -4.1; 3270 -3.5; 3597 -2.7; 3957 -2.8; 4353 -3.9; 4788 -5.3; 5267 -5.7; 5793 -2.3; 6373 0.2; 7010 -0.3; 7711 -4.0; 8482 -4.8; 9330 -0.8; 10263 0.0; 11289 -2.7; 12418 -6.8; 13660 -9.4; 15026 -11.8; 16529 -10.1; 18182 -4.0; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Pinnacle PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Pinnacle PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 172 Hz   | 0.44 | -7.0 dB  |
| Peaking | 3021 Hz  | 3.92 | -3.9 dB  |
| Peaking | 4936 Hz  | 3.95 | -5.6 dB  |
| Peaking | 15231 Hz | 1.53 | -12.7 dB |
| Peaking | 24000 Hz | 0.88 | -10.7 dB |
| Peaking | 910 Hz   | 3.34 | 1.3 dB   |
| Peaking | 1831 Hz  | 3.48 | 1.7 dB   |
| Peaking | 6783 Hz  | 3.18 | 6.2 dB   |
| Peaking | 8280 Hz  | 1.48 | -7.5 dB  |
| Peaking | 9786 Hz  | 3.11 | 7.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Mee%20Audio%20Pinnacle%20PX/Mee%20Audio%20Pinnacle%20PX.png)