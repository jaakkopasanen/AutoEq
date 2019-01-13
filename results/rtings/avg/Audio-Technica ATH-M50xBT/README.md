# Audio-Technica ATH-M50xBT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 -2.9; 23 -3.2; 25 -3.5; 28 -3.9; 31 -4.3; 34 -4.5; 37 -4.6; 41 -4.6; 45 -4.4; 49 -4.1; 54 -3.4; 60 -3.0; 66 -3.3; 72 -3.8; 79 -4.4; 87 -5.1; 96 -5.6; 106 -5.9; 116 -6.0; 128 -6.0; 141 -5.9; 155 -5.7; 170 -5.4; 187 -4.8; 206 -3.9; 227 -2.9; 249 -1.9; 274 -0.6; 302 2.0; 332 3.1; 365 4.0; 402 4.2; 442 4.3; 486 4.0; 535 3.3; 588 2.7; 647 2.1; 712 1.6; 783 1.6; 861 1.6; 947 0.5; 1042 -0.3; 1146 -0.8; 1261 -1.5; 1387 -2.1; 1526 -2.7; 1678 -3.2; 1846 -3.0; 2031 -2.9; 2234 -2.8; 2457 -2.3; 2703 -2.9; 2973 -3.2; 3270 -2.4; 3597 -0.8; 3957 -1.8; 4353 -4.8; 4788 -2.0; 5267 1.8; 5793 5.0; 6373 3.8; 7010 1.5; 7711 -1.1; 8482 -2.9; 9330 -3.7; 10263 -4.7; 11289 -6.2; 12418 -5.5; 13660 -3.4; 15026 -3.4; 16529 -3.3; 18182 -1.7; 20000 -2.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50xBT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50xBT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 1.12 | -3.8 dB |
| Peaking | 163 Hz   | 0.54 | -7.7 dB |
| Peaking | 391 Hz   | 0.88 | 8.2 dB  |
| Peaking | 6085 Hz  | 2.29 | 11.1 dB |
| Peaking | 7300 Hz  | 0.26 | -5.9 dB |
| Peaking | 849 Hz   | 6.94 | 1.1 dB  |
| Peaking | 1591 Hz  | 2.86 | -1.3 dB |
| Peaking | 3928 Hz  | 2.81 | 3.7 dB  |
| Peaking | 4329 Hz  | 5.94 | -5.5 dB |
| Peaking | 11586 Hz | 6.54 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M50xBT/Audio-Technica%20ATH-M50xBT.png)