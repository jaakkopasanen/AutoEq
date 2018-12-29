# Audio-Technica ATH-M40x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 21 0.0; 23 0.7; 25 0.1; 28 -0.7; 31 -1.3; 34 -1.8; 37 -2.2; 41 -2.6; 45 -2.9; 49 -3.1; 54 -3.2; 60 -3.3; 66 -3.4; 72 -3.3; 79 -3.0; 87 -3.2; 96 -4.0; 106 -4.9; 116 -5.6; 128 -5.7; 141 -5.3; 155 -5.0; 170 -4.8; 187 -4.1; 206 -3.1; 227 -1.9; 249 -0.8; 274 0.2; 302 1.1; 332 1.9; 365 1.8; 402 1.2; 442 1.2; 486 1.1; 535 0.8; 588 0.6; 647 0.6; 712 0.6; 783 0.6; 861 0.7; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.5; 1387 -1.7; 1526 -1.9; 1678 -2.2; 1846 -2.2; 2031 -2.1; 2234 -1.3; 2457 -0.2; 2703 0.2; 2973 -0.3; 3270 -1.1; 3597 -1.2; 3957 -1.4; 4353 -2.5; 4788 -1.0; 5267 0.4; 5793 1.8; 6373 1.1; 7010 -0.9; 7711 -3.7; 8482 -5.6; 9330 -6.3; 10263 -5.7; 11289 -4.0; 12418 -2.9; 13660 -5.3; 15026 -9.4; 16529 -8.7; 18182 -5.2; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M40x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-22**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M40x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 56 Hz    | 1.1  | -3.0 dB |
| Peaking | 135 Hz   | 1.64 | -5.7 dB |
| Peaking | 1725 Hz  | 2.32 | -2.4 dB |
| Peaking | 9216 Hz  | 3.24 | -5.7 dB |
| Peaking | 16112 Hz | 1.25 | -9.6 dB |
| Peaking | 198 Hz   | 3.24 | -1.9 dB |
| Peaking | 348 Hz   | 1.51 | 2.4 dB  |
| Peaking | 809 Hz   | 4.03 | 0.8 dB  |
| Peaking | 4318 Hz  | 4.6  | -2.2 dB |
| Peaking | 5959 Hz  | 5.02 | 3.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M40x/Audio-Technica%20ATH-M40x.png)