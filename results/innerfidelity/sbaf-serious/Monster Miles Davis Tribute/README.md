# Monster Miles Davis Tribute
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 -9.4; 23 -9.4; 25 -9.3; 28 -9.2; 31 -9.1; 34 -9.0; 37 -8.9; 41 -8.7; 45 -8.6; 49 -8.4; 54 -8.3; 60 -8.2; 66 -8.2; 72 -8.1; 79 -8.1; 87 -8.1; 96 -7.9; 106 -7.8; 116 -7.5; 128 -7.3; 141 -7.0; 155 -6.8; 170 -6.3; 187 -5.9; 206 -5.4; 227 -4.9; 249 -4.4; 274 -4.0; 302 -3.5; 332 -3.0; 365 -2.4; 402 -1.9; 442 -1.3; 486 -0.9; 535 -0.5; 588 0.2; 647 0.6; 712 0.7; 783 0.9; 861 0.7; 947 0.3; 1042 -0.3; 1146 -0.7; 1261 -1.3; 1387 -2.2; 1526 -3.3; 1678 -4.2; 1846 -4.8; 2031 -5.4; 2234 -5.9; 2457 -5.3; 2703 -4.8; 2973 -1.5; 3270 1.3; 3597 2.6; 3957 1.5; 4353 -1.3; 4788 -2.5; 5267 -0.9; 5793 1.9; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.2; 15026 -1.0; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Miles Davis Tribute GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Miles Davis Tribute ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.2  | -9.1 dB |
| Peaking | 157 Hz   | 0.8  | -3.6 dB |
| Peaking | 2270 Hz  | 1.54 | -6.4 dB |
| Peaking | 3486 Hz  | 4.84 | 5.3 dB  |
| Peaking | 6468 Hz  | 6.42 | 5.0 dB  |
| Peaking | 317 Hz   | 2.23 | -0.8 dB |
| Peaking | 757 Hz   | 1.33 | 1.8 dB  |
| Peaking | 1580 Hz  | 4.12 | -1.2 dB |
| Peaking | 4736 Hz  | 8.15 | -2.8 dB |
| Peaking | 14682 Hz | 7.59 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Miles%20Davis%20Tribute/Monster%20Miles%20Davis%20Tribute.png)