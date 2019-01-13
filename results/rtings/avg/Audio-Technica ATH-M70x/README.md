# Audio-Technica ATH-M70x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 21 0.0; 23 1.2; 25 1.0; 28 0.7; 31 0.6; 34 0.6; 37 0.7; 41 0.9; 45 0.9; 49 0.9; 54 0.8; 60 0.5; 66 0.0; 72 -0.4; 79 -0.9; 87 -1.3; 96 -1.6; 106 -1.9; 116 -2.1; 128 -2.1; 141 -2.0; 155 -1.9; 170 -1.7; 187 -1.7; 206 -1.6; 227 -1.9; 249 -2.1; 274 -2.4; 302 -2.0; 332 -2.5; 365 -2.4; 402 -1.8; 442 -1.2; 486 -0.9; 535 -0.6; 588 0.9; 647 1.6; 712 1.5; 783 1.0; 861 0.6; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.0; 1526 -1.7; 1678 -2.5; 1846 -3.6; 2031 -4.7; 2234 -4.7; 2457 -4.4; 2703 -3.9; 2973 -4.2; 3270 -5.9; 3597 -6.4; 3957 -6.1; 4353 -8.8; 4788 -8.8; 5267 -6.5; 5793 -3.6; 6373 -2.5; 7010 -3.2; 7711 -5.7; 8482 -7.9; 9330 -7.7; 10263 -6.4; 11289 -4.9; 12418 -2.4; 13660 -0.4; 15026 -0.8; 16529 -2.9; 18182 -4.5; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M70x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 192 Hz   | 0.72 | -2.3 dB |
| Peaking | 2206 Hz  | 2.01 | -4.1 dB |
| Peaking | 4409 Hz  | 2.09 | -8.1 dB |
| Peaking | 9271 Hz  | 2.21 | -7.7 dB |
| Peaking | 18769 Hz | 1.54 | -5.0 dB |
| Peaking | 22 Hz    | 1.42 | 1.4 dB  |
| Peaking | 49 Hz    | 2.89 | 1.2 dB  |
| Peaking | 367 Hz   | 2.69 | -1.4 dB |
| Peaking | 690 Hz   | 2.57 | 2.4 dB  |
| Peaking | 6315 Hz  | 7.81 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M70x/Audio-Technica%20ATH-M70x.png)