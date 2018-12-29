# Audio-Technica ATH-M60x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.5; 28 1.3; 31 1.1; 34 0.9; 37 0.9; 41 0.7; 45 0.5; 49 0.4; 54 0.2; 60 0.1; 66 -0.1; 72 -0.2; 79 -0.5; 87 -0.7; 96 -0.9; 106 -1.1; 116 -1.3; 128 -1.5; 141 -1.6; 155 -1.7; 170 -1.7; 187 -1.6; 206 -1.3; 227 -1.0; 249 -0.5; 274 -0.0; 302 0.8; 332 2.3; 365 4.5; 402 6.0; 442 6.0; 486 5.2; 535 2.8; 588 1.1; 647 0.3; 712 -0.0; 783 -0.1; 861 0.0; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.1; 1387 -0.1; 1526 0.1; 1678 -0.3; 1846 -0.5; 2031 -0.1; 2234 1.3; 2457 2.9; 2703 3.1; 2973 3.4; 3270 3.3; 3597 2.8; 3957 -0.9; 4353 -2.7; 4788 0.1; 5267 2.3; 5793 3.0; 6373 0.6; 7010 -2.4; 7711 -1.0; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -2.6; 15026 -6.5; 16529 -6.1; 18182 -4.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M60x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M60x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 2    | 1.7 dB  |
| Peaking | 428 Hz   | 3.3  | 7.0 dB  |
| Peaking | 2934 Hz  | 2.9  | 4.1 dB  |
| Peaking | 12163 Hz | 1.22 | 5.4 dB  |
| Peaking | 15773 Hz | 0.69 | -8.5 dB |
| Peaking | 157 Hz   | 1.29 | -2.0 dB |
| Peaking | 1833 Hz  | 4.64 | -1.1 dB |
| Peaking | 4358 Hz  | 5.75 | -5.4 dB |
| Peaking | 5768 Hz  | 1.75 | 4.5 dB  |
| Peaking | 6971 Hz  | 4.33 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M60x/Audio-Technica%20ATH-M60x.png)