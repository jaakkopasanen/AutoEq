# Audio Technica ATH-ANC9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 -5.9; 23 -6.3; 25 -6.7; 28 -7.0; 31 -7.1; 34 -6.9; 37 -6.5; 41 -5.6; 45 -4.5; 49 -3.6; 54 -2.8; 60 -2.2; 66 -1.9; 72 -1.9; 79 -2.2; 87 -2.7; 96 -3.3; 106 -3.5; 116 -3.6; 128 -3.7; 141 -3.4; 155 -3.0; 170 -2.4; 187 -1.6; 206 -1.0; 227 -0.2; 249 0.3; 274 0.8; 302 1.4; 332 1.9; 365 2.2; 402 2.1; 442 2.5; 486 2.5; 535 2.8; 588 3.5; 647 4.3; 712 4.9; 783 5.1; 861 4.0; 947 1.9; 1042 -1.3; 1146 -4.6; 1261 -7.7; 1387 -9.1; 1526 -9.4; 1678 -7.6; 1846 -6.3; 2031 -5.0; 2234 -5.3; 2457 -4.7; 2703 -5.1; 2973 -5.9; 3270 -6.3; 3597 -6.4; 3957 -6.6; 4353 -6.4; 4788 -5.2; 5267 -4.1; 5793 -3.6; 6373 0.3; 7010 1.0; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 1    | -7.4 dB  |
| Peaking | 129 Hz  | 1.4  | -3.8 dB  |
| Peaking | 863 Hz  | 0.84 | 11.6 dB  |
| Peaking | 1348 Hz | 1.14 | -16.0 dB |
| Peaking | 3902 Hz | 1.76 | -6.0 dB  |
| Peaking | 10 Hz   | 1.52 | -1.0 dB  |
| Peaking | 335 Hz  | 3.48 | 0.8 dB   |
| Peaking | 533 Hz  | 4.84 | -0.8 dB  |
| Peaking | 5706 Hz | 3.47 | -3.6 dB  |
| Peaking | 6560 Hz | 2.68 | 4.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC9/Audio%20Technica%20ATH-ANC9.png)