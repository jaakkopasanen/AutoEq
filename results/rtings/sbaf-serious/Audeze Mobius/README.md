# Audeze Mobius

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.8; 23 -1.6; 25 -1.4; 28 -1.2; 31 -1.2; 34 -1.3; 37 -1.5; 41 -1.6; 45 -1.5; 49 -1.3; 54 -1.0; 60 -0.7; 66 -0.5; 72 -0.3; 79 -0.1; 87 0.0; 96 -0.0; 106 -0.1; 116 -0.3; 128 -0.4; 141 -0.6; 155 -0.7; 170 -0.8; 187 -0.8; 206 -0.9; 227 -0.9; 249 -0.7; 274 -0.4; 302 0.0; 332 0.5; 365 0.9; 402 1.4; 442 1.7; 486 1.3; 535 0.7; 588 0.2; 647 0.4; 712 0.4; 783 -0.3; 861 -0.5; 947 -0.2; 1042 0.1; 1146 -0.2; 1261 -0.4; 1387 -0.5; 1526 -1.2; 1678 -1.9; 1846 -2.2; 2031 -1.7; 2234 -1.0; 2457 -0.8; 2703 -1.0; 2973 -0.8; 3270 -0.3; 3597 2.1; 3957 5.9; 4353 5.6; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.9; 9330 -3.1; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -2.6; 18182 -2.8; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Mobius GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Mobius ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.47 | -1.6 dB |
| Peaking | 2925 Hz  | 0.84 | -8.7 dB |
| Peaking | 4520 Hz  | 0.7  | 11.8 dB |
| Peaking | 8757 Hz  | 2.65 | -7.3 dB |
| Peaking | 17924 Hz | 1.15 | -3.4 dB |
| Peaking | 212 Hz   | 1.92 | -1.0 dB |
| Peaking | 431 Hz   | 2.55 | 1.8 dB  |
| Peaking | 1800 Hz  | 3.23 | -2.0 dB |
| Peaking | 2359 Hz  | 1.18 | 1.3 dB  |
| Peaking | 3232 Hz  | 6.38 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audeze%20Mobius/Audeze%20Mobius.png)