# Audio-Technica ATH-ANC23

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.6; 49 5.2; 54 4.7; 60 3.9; 66 3.1; 72 2.5; 79 1.8; 87 0.9; 96 0.0; 106 -0.9; 116 -1.9; 128 -2.8; 141 -3.6; 155 -4.3; 170 -4.9; 187 -5.3; 206 -5.7; 227 -6.0; 249 -6.1; 274 -6.2; 302 -6.3; 332 -6.3; 365 -6.3; 402 -6.1; 442 -5.8; 486 -5.3; 535 -4.5; 588 -3.4; 647 -2.1; 712 -1.8; 783 -1.1; 861 -0.6; 947 -0.2; 1042 0.1; 1146 0.1; 1261 -0.3; 1387 -1.3; 1526 -2.5; 1678 -3.0; 1846 -2.8; 2031 -2.0; 2234 -0.5; 2457 0.8; 2703 0.8; 2973 -0.2; 3270 -1.7; 3597 -2.8; 3957 -3.5; 4353 -4.4; 4788 -5.4; 5267 -7.2; 5793 -7.9; 6373 -6.0; 7010 -3.2; 7711 -2.1; 8482 -3.4; 9330 -2.7; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.5; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC23 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC23 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.4  | 6.7 dB  |
| Peaking | 196 Hz   | 0.64 | -6.3 dB |
| Peaking | 412 Hz   | 1.53 | -3.6 dB |
| Peaking | 5495 Hz  | 1.97 | -7.8 dB |
| Peaking | 8692 Hz  | 6.83 | -2.1 dB |
| Peaking | 1132 Hz  | 1.81 | 2.1 dB  |
| Peaking | 1755 Hz  | 1.63 | -3.9 dB |
| Peaking | 2578 Hz  | 2.18 | 3.3 dB  |
| Peaking | 3527 Hz  | 3.47 | -1.5 dB |
| Peaking | 10927 Hz | 3.81 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC23/Audio-Technica%20ATH-ANC23.png)