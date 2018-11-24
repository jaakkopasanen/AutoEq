# Audio Technica ATH CKX5iS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 21 -6.8; 23 -6.8; 25 -6.9; 28 -6.8; 31 -6.8; 34 -6.8; 37 -6.8; 41 -6.8; 45 -6.8; 49 -6.7; 54 -6.7; 60 -6.6; 66 -6.6; 72 -6.7; 79 -6.7; 87 -6.7; 96 -6.7; 106 -6.5; 116 -6.3; 128 -6.2; 141 -5.9; 155 -5.6; 170 -5.3; 187 -4.9; 206 -4.5; 227 -3.9; 249 -3.5; 274 -3.0; 302 -2.5; 332 -2.0; 365 -1.5; 402 -1.0; 442 -0.5; 486 -0.2; 535 0.2; 588 0.8; 647 1.0; 712 1.0; 783 1.2; 861 0.8; 947 0.4; 1042 -0.3; 1146 -0.8; 1261 -1.5; 1387 -2.2; 1526 -3.4; 1678 -4.1; 1846 -4.2; 2031 -3.5; 2234 -4.1; 2457 -4.5; 2703 -5.6; 2973 -5.5; 3270 -4.0; 3597 -2.3; 3957 -2.7; 4353 -5.1; 4788 -7.3; 5267 -8.5; 5793 -6.8; 6373 -3.4; 7010 -0.7; 7711 0.2; 8482 -0.1; 9330 -2.5; 10263 -5.7; 11289 -4.9; 12418 -2.9; 13660 -4.8; 15026 -3.5; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH CKX5iS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH CKX5iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.25 | -7.3 dB |
| Peaking | 1715 Hz  | 3.22 | -3.6 dB |
| Peaking | 2750 Hz  | 2.6  | -5.1 dB |
| Peaking | 5189 Hz  | 3.5  | -8.5 dB |
| Peaking | 12248 Hz | 1.45 | -4.7 dB |
| Peaking | 21 Hz    | 2.91 | -1.4 dB |
| Peaking | 679 Hz   | 1.9  | 2.1 dB  |
| Peaking | 7950 Hz  | 4.1  | 2.6 dB  |
| Peaking | 10288 Hz | 7.02 | -3.1 dB |
| Peaking | 16739 Hz | 5.66 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH%20CKX5iS/Audio%20Technica%20ATH%20CKX5iS.png)