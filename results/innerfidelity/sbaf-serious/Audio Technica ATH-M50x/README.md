# Audio Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.4; 25 -1.8; 28 -2.2; 31 -2.6; 34 -2.8; 37 -3.0; 41 -3.1; 45 -3.2; 49 -3.2; 54 -3.0; 60 -2.9; 66 -2.6; 72 -1.7; 79 -0.5; 87 0.3; 96 0.1; 106 -1.5; 116 -2.1; 128 -3.1; 141 -4.0; 155 -3.4; 170 -1.9; 187 -2.9; 206 -1.9; 227 -0.6; 249 0.5; 274 1.7; 302 2.4; 332 2.3; 365 2.0; 402 1.6; 442 1.2; 486 0.6; 535 0.1; 588 0.2; 647 -0.1; 712 -0.4; 783 -0.3; 861 -0.4; 947 -0.0; 1042 0.1; 1146 0.4; 1261 -0.1; 1387 -1.0; 1526 -2.0; 1678 -2.8; 1846 -3.2; 2031 -2.7; 2234 -2.1; 2457 -0.6; 2703 0.6; 2973 2.5; 3270 3.5; 3597 4.0; 3957 2.2; 4353 -0.1; 4788 2.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 1.25 | -3.5 dB |
| Peaking | 144 Hz   | 3.15 | -4.0 dB |
| Peaking | 1884 Hz  | 2.57 | -3.7 dB |
| Peaking | 3350 Hz  | 3.97 | 4.2 dB  |
| Peaking | 5777 Hz  | 3.34 | 6.8 dB  |
| Peaking | 90 Hz    | 7.44 | 1.6 dB  |
| Peaking | 196 Hz   | 4.65 | -2.2 dB |
| Peaking | 321 Hz   | 2.12 | 2.8 dB  |
| Peaking | 1168 Hz  | 7.91 | 0.9 dB  |
| Peaking | 24000 Hz | 1.79 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)